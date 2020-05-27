path = '../'
with open("../lists/train_list.txt","w") as f:
    # for i in range(65):
    #     f.write(f'{path}data_deep/data1/imu/{i}.csv\n')
    # for i in range(85):
    #     f.write(f'{path}data_deep/data2/imu/{i}.csv\n')
    # for i in range(90):
    #     f.write(f'{path}data_deep/data3/imu/{i}.csv\n')
    for i in range(125):
        f.write(f'{path}data_deep/data4/imu/{i}.csv\n')
    for i in range(125):
        f.write(f'{path}data_deep/data5/imu/{i}.csv\n')
    for i in range(27):
        f.write(f'{path}data_deep/data6/imu/{i}.csv\n')
    for i in range(95):
        f.write(f'{path}data_deep/data7/imu/{i}.csv\n')
    for i in range(120):
        f.write(f'{path}data_deep/data8/imu/{i}.csv\n')

with open("val_list.txt","w") as f:
    # for i in range(65, 69):
    #     f.write(f'{path}data_deep/data1/imu/{i}.csv\n')
    # for i in range(85, 90):
    #     f.write(f'{path}data_deep/data2/imu/{i}.csv\n')
    # for i in range(90, 95):
    #     f.write(f'{path}data_deep/data3/imu/{i}.csv\n')
    for i in range(125, 143):
        f.write(f'{path}data_deep/data4/imu/{i}.csv\n')
    for i in range(125, 143):
        f.write(f'{path}data_deep/data5/imu/{i}.csv\n')
    for i in range(27, 30):
        f.write(f'{path}data_deep/data6/imu/{i}.csv\n')
    for i in range(95, 113):
        f.write(f'{path}data_deep/data7/imu/{i}.csv\n')
    for i in range(120, 137):
        f.write(f'{path}data_deep/data8/imu/{i}.csv\n')

with open("test_list.txt","w") as f:
    # for i in range(69, 73):
    #     f.write(f'{path}data_deep/data1/imu/{i}.csv\n')
    # for i in range(90, 95):
    #     f.write(f'{path}data_deep/data2/imu/{i}.csv\n')
    # for i in range(95, 100):
    #     f.write(f'{path}data_deep/data3/imu/{i}.csv\n')
    for i in range(143, 151):
        f.write(f'{path}data_deep/data4/imu/{i}.csv\n')
    for i in range(143, 151):
        f.write(f'{path}data_deep/data5/imu/{i}.csv\n')
    for i in range(30, 31):
        f.write(f'{path}data_deep/data6/imu/{i}.csv\n')
    for i in range(113, 120):
        f.write(f'{path}data_deep/data7/imu/{i}.csv\n')
    for i in range(137, 144):
        f.write(f'{path}data_deep/data8/imu/{i}.csv\n')