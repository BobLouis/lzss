import numpy as np

# Function to convert integer to 8-bit binary
def int_to_8bit_binary(integer):
    return [int(bit) for bit in format(integer, '08b')]
def file2arr():
    # Read the binary file
    with open('output.txt', 'rb') as f:
        byte_data = f.read()

    # Initialize an empty list to store each 8-bit array
    binary_list = []

    # Convert byte data to 8-bit binary and store in the list
    for byte in byte_data:
        binary_list.append(int_to_8bit_binary(byte))

    # Convert the list of 8-bit binary arrays to a NumPy array
    binary_array = np.array(binary_list, dtype=np.uint8)

    # Validate if we have 643 rows to form the 2D array
    if binary_array.shape[0] != 643:
        print(f"Warning: Expected 643 rows, but got {binary_array.shape[0]}.")

    print("origin 2D NumPy array:")
    for i in range (binary_array.shape[0]):
        print(i," ", binary_array[i])
    # print(binary_array[0])
    # print(binary_array[1])
    # print(binary_array[2])
    return binary_array

def mask_dont_care(data_2d):
    
    dont_care_bit = 0

    # reverse
    data_2d = data_2d[:, ::-1]
    data_2d = np.vectorize(str)(data_2d)
    print("reverse", data_2d)

    data_2d_org = data_2d.copy()

    # Check addr_7
    addr_7_bit_4 = data_2d[7, 4]
    addr_7_bit_5 = data_2d[7, 5]


# addr_8 ~ addr_22, N=0~4:
    for N in range(5):
        # Check addr_(8+N*3)
        if np.all(data_2d_org[143+N*20] == '0'):
            data_2d[8+N*3, :] = 'x'
            dont_care_bit += 8
            print(f"mask data_2d[{8+N*3}, :] = data_2d[{7+N*3}, 0]")

        if np.all(data_2d_org[144+N*20] == '0'):
            data_2d[8+N*3, 4:] = 'x'
            dont_care_bit += 4
            print(f"mask data_2d[{8+N*3}, 4:] = data_2d[{7+N*3}, 0]")

            
        if np.all(data_2d_org[145+N*20] == '0'):
            data_2d[8+N*3, :4] = 'x'
            dont_care_bit += 4
            print(f"mask data_2d[{8+N*3}, :4] = data_2d[{8+N*3}, 4]")


        # Check addr_(9+N*3)
        if np.all(data_2d_org[143+N*20] == '0'):
            data_2d[9+N*3, 4:] = 'x'
            dont_care_bit += 4
            print(f"mask data_2d[{9+N*3}, 4:] = data_2d[{8+N*3}, 0]")
            
        if np.all(data_2d_org[146+N*20] == '0'):
            data_2d[9+N*3, 4:] = 'x'
            dont_care_bit += 4
            print(f"mask data_2d[{9+N*3}, 4:] = data_2d[{8+N*3}, 0]")


        if np.all(data_2d_org[153+N*20] == '0'):
            data_2d[9+N*3, :4] = 'x'
            dont_care_bit += 4
            print(f"mask data_2d[{9+N*3}, :4] = data_2d[{9+N*3}, 4]")
            

        if np.all(data_2d_org[154+N*20] == '0'):
            data_2d[9+N*3, :4] = 'x'
            dont_care_bit += 4
            print(f"mask data_2d[{9+N*3}, :4] = data_2d[{9+N*3}, 4]")


        # Check addr_(10+N*3)

        if np.all(data_2d_org[153+N*20] == '0'):
            data_2d[10+N*3, :] = 'x'
            dont_care_bit += 8
            print(f"mask data_2d[{10+N*3}, :] = data_2d[{9+N*3}, 0]")


        if np.all(data_2d_org[155+N*20] == '0'):
            data_2d[10+N*3, 4:] = 'x'
            dont_care_bit += 4
            print(f"mask data_2d[{10+N*3}, 4:] = data_2d[{9+N*3}, 0]")

        if np.all(data_2d_org[156+N*20] == '0'):
            data_2d[10+N*3, :4] = 'x'
            dont_care_bit += 4
            print(f"mask data_2d[{10+N*3}, :4] = data_2d[{10+N*3}, 4]")



    # addr_23 ~ addr_142, N=0~9:
    # Loop through each byte
    ## don't care bit 3 &7

    for n in range (23, 143):
        data_2d[n,7] = 'x'
        data_2d[n,3] = 'x'
    dont_care_bit += 240
    
                
    # addr_143 ~ addr_242, 
    # Loop through each byte
    for N in range(10):
        # Check addr_(143+N*10)
        if np.all(data_2d_org[143+N*10] == '0'):
            for i in range(144+N*10, 153+N*10):
                data_2d[i, :] = 'x'
                dont_care_bit += 8
                print(f"mask data_2d[{i}, :] = data_2d[{143+N*10}, 0]")

            continue

        # Check addr_(144+N*10)
        if np.all(data_2d_org[144+N*10] == '0'):
            for i in range(147+N*10, 149+N*10):
                data_2d[i, :] = 'x'
                print(f"mask data_2d[{i}, :] = data_2d[{146+N*10}, 0]")

                dont_care_bit += 8

        # Check addr_(145+N*10)
        if np.all(data_2d_org[145+N*10] == '0'):
            for i in range(149+N*10, 151+N*10):
                data_2d[i, :] = 'x'
                print(f"mask data_2d[{i}, :] = data_2d[{148+N*10}, 0]")

                dont_care_bit += 8

        # Check addr_(146+N*10)
        if np.all(data_2d_org[146+N*10] == '0'):
            for i in range(151+N*10, 153+N*10):
                data_2d[i, :] = 'x'
                print(f"mask data_2d[{i}, :] = data_2d[{150+N*10}, 0]")

                dont_care_bit += 8


    #addr_243 ~ addr_342, 
    # Loop through each byte
    for N in range(10):
        # Check addr_(243+N*10)
        if np.all(data_2d_org[243+N*10] == '0'):
            for i in range(244+N*10, 253+N*10):
                data_2d[i, :] = 'x'
                dont_care_bit += 8
                print(f"mask data_2d[{i}, :] = data_2d[{243+N*10}, 0]")

            continue
            

        # Check addr_(244+N*10)
        if np.all(data_2d_org[244+N*10] == '0'):
            for i in range(247+N*10, 249+N*10):
                data_2d[i, :] = 'x'
                dont_care_bit += 8
                print(f"mask data_2d[{i}, :] = data_2d[{246+N*10}, 0]")


        # Check addr_(245+N*10)
        if np.all(data_2d_org[245+N*10] == '0'):
            for i in range(249+N*10, 251+N*10):
                data_2d[i, :] = 'x'
                print(f"mask data_2d[{i}, :] = data_2d[{248+N*10}, 0]")
                dont_care_bit += 8

        # Check addr_(246+N*10)
        if np.all(data_2d_org[246+N*10] == '0'):
            for i in range(251+N*10, 253+N*10):
                data_2d[i, :] = 'x'
                dont_care_bit += 8
                print(f"mask data_2d[{i}, :] = data_2d[{250+N*10}, 0]")


    # addr_343 ~ addr_442
    # Loop through each byte
    for N in range(10):
        # Check addr_(343+N*10)
        if np.all(data_2d_org[343+N*10] == '0'):
            for i in range(344+N*10, 353+N*10):
                data_2d[i, :] = 'x'
                print(f"mask data_2d[{i}, :] = data_2d[{343+N*10}, 0]")
                dont_care_bit += 8
            continue
            

        # Check addr_(344+N*10)
        if np.all(data_2d_org[344+N*10] == '0'):
            for i in range(347+N*10, 349+N*10):
                data_2d[i, :] = 'x'
                dont_care_bit += 8
                print(f"mask data_2d[{i}, :] = data_2d[{346+N*10}, 0]")

        # Check addr_(345+N*10)
        if np.all(data_2d_org[345+N*10] == '0'):
            for i in range(349+N*10, 351+N*10):
                data_2d[i, :] = 'x'
                dont_care_bit += 8
                print(f"mask data_2d[{i}, :] = data_2d[{348+N*10}, 0]")

        # Check addr_(346+N*10)
        if np.all(data_2d_org[346+N*10] == '0'):
            for i in range(351+N*10, 353+N*10):
                data_2d[i, :] = 'x'
                dont_care_bit += 8
                print(f"mask data_2d[{i}, :] = data_2d[{350+N*10}, 0]")

    # addr_443 ~ addr_542, N=0~9:
    # Iterate over each byte
    for N in range(10):
        # If addr_(443+N*10) equals 0
        if np.all(data_2d_org[443+N*10] == '0'):
            for i in range(444+N*10, 453+N*10):
                data_2d[i,:] = 'x'
                print(f"mask data_2d[{i},:] = data_2d[{443+N*10},0]")
                dont_care_bit += 8
            continue

        # If addr_(444+N*10) equals 0
        if np.all(data_2d_org[444+N*10] == '0'):
            for i in range(447+N*10, 449+N*10):
                data_2d[i,:] = 'x'
                print(f"mask data_2d[{i},:] = data_2d[{446+N*10},0]")
                dont_care_bit += 8

        # If addr_(445+N*10) equals 0
        if np.all(data_2d_org[445+N*10] == '0'):
            for i in range(449+N*10, 451+N*10):
                data_2d[i,:] = 'x'
                print(f"mask data_2d[{i},:] = data_2d[{448+N*10},0]")
                dont_care_bit += 8

        # If addr_(446+N*10) equals 0
        if np.all(data_2d_org[446+N*10] == '0'):
            for i in range(451+N*10, 453+N*10):
                data_2d[i,:] = 'x'
                print(f"mask data_2d[{i},:] = data_2d[{450+N*10},0]")
                dont_care_bit += 8


    # addr_543 ~ addr_642, N=0~9:
    # Iterate over each byte
    for N in range(10):
        # If addr_(543+N*10) equals 0
        if np.all(data_2d_org[543+N*10] == '0'):
            for i in range(544+N*10, 553+N*10):
                data_2d[i,:] = 'x'
                print(f"mask data_2d[{i},:] = data_2d[{543+N*10},0]")
                dont_care_bit += 8
            continue


        # If addr_(544+N*10) equals 0
        if np.all(data_2d_org[544+N*10] == '0'):
            for i in range(547+N*10, 549+N*10):
                data_2d[i,:] = 'x'
                print(f"mask data_2d[{i},:] = data_2d[{546+N*10},0]")
                dont_care_bit += 8

        # If addr_(545+N*10) equals 0
        if np.all(data_2d_org[545+N*10] == '0'):
            for i in range(549+N*10, 551+N*10):
                data_2d[i,:] = 'x'
                print(f"mask data_2d[{i},:] = data_2d[{548+N*10},0]")
                dont_care_bit += 8

        # If addr_(546+N*10) equals 0
        if np.all(data_2d_org[546+N*10] == '0'):
            for i in range(551+N*10, 553+N*10):
                data_2d[i,:] = 'x'
                print(f"mask data_2d[{i},:] = data_2d[{545+N*10},0]")
                dont_care_bit += 8
    
    print('dont care bit', dont_care_bit)
    print('dont care bit ratio', dont_care_bit/5144)

    # reverse back
    data_2d = data_2d[:, ::-1]


    print('mask complete')
    for i in range (data_2d.shape[0]):
        print(i," ", data_2d[i])

    np.savetxt('output_x.txt', data_2d, fmt="%s", delimiter="")


if __name__ == '__main__':
    arr = file2arr()
    mask_dont_care(arr)
