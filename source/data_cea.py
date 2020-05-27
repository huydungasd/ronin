from os import path as osp
import sys

import pandas
import numpy as np
import quaternion

from data_utils import CompiledSequence


class CEAGlobSpeedSequence(CompiledSequence):
    """
    Dataset :- RIDI (can be downloaded from https://wustl.app.box.com/s/6lzfkaw00w76f8dmu0axax7441xcrzd9)
    Features :- raw angular rate and acceleration (includes gravity).
    """
    feature_dim = 6
    target_dim = 3
    aux_dim = 8

    def __init__(self, data_path, **kwargs):
        super().__init__(**kwargs)
        self.ts, self.features, self.targets, self.orientations, self.gt_pos = None, None, None, None, None
        self.w = kwargs.get('interval', 1)
        self.info = {}

        if data_path is not None:
            self.load(data_path)

    def load(self, path):
        if path[-1] == '/':
            path = path[:-1]

        self.info['path'] = osp.split(path)[-1]
        self.info['ori_source'] = 'game_rv'

        # data_files = [name for name in os.listdir(path) if os.path.isfile(osp.join(path, name))]
        imu_all = pandas.read_csv(path)
        str_tmp = path.split('/')
        str_tmp[-2] = 'gt'
        gt_all = pandas.read_csv('/'.join(str_tmp))

        ts = imu_all[['time']].values
        gyro = imu_all[['gyr_x', 'gyr_y', 'gyr_z']].values
        acce = imu_all[['acc_x', 'acc_y', 'acc_z']].values
        tango_pos = gt_all[['pos_x', 'pos_y', 'pos_z']].values

        # Use game rotation vector as device orientation.
        init_tango_ori = quaternion.quaternion(*gt_all[['q', 'p1', 'p2', 'p3']].values[0])
        game_rv = quaternion.from_float_array(gt_all[['q', 'p1', 'p2', 'p3']].values)

        # init_rotor = init_tango_ori * game_rv[0].conj()
        # ori = init_rotor * game_rv

        # nz = np.zeros(ts.shape)
        # gyro_q = quaternion.from_float_array(np.concatenate([nz, gyro], axis=1))
        # acce_q = quaternion.from_float_array(np.concatenate([nz, acce], axis=1))

        # gyro_glob = quaternion.as_float_array(ori * gyro_q * ori.conj())[:, 1:]
        # acce_glob = quaternion.as_float_array(ori * acce_q * ori.conj())[:, 1:]
        gyro_glob = gyro
        acce_glob = acce

        self.ts = ts
        self.features = np.concatenate([gyro_glob, acce_glob], axis=1)
        self.targets = (tango_pos[self.w:, :3] - tango_pos[:-self.w, :3]) / (ts[self.w:] - ts[:-self.w])
        self.gt_pos = tango_pos
        self.orientations = quaternion.as_float_array(game_rv)
        print(self.ts.shape, self.features.shape, self.targets.shape, self.gt_pos.shape, self.orientations.shape,
              self.w)

    def get_feature(self):
        return self.features

    def get_target(self):
        return self.targets

    def get_aux(self):
        return np.concatenate([self.ts, self.orientations, self.gt_pos], axis=1)

    def get_meta(self):
        return '{}: orientation {}'.format(self.info['path'], self.info['ori_source'])