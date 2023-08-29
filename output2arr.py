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

    print("2D NumPy array:")
    print(binary_array[0])
    print(binary_array[1])
    print(binary_array[2])
    return binary_array

def check_dont_care(data_2d):
    
    dont_care_bit = 0

    # reverse
    data_2d = data_2d[:, ::-1]
    print("reverse", data_2d[0])


    #addr 0
    # print("addr 0")
    # if np.all(data_2d[0, 5:] == 0):
    #     print("Pass")
    # else:
    #     print("Error")


    # Check addr_7
    addr_7_bit_4 = data_2d[7, 4]
    addr_7_bit_5 = data_2d[7, 5]

    # Check addr_8 ~ addr_22 if addr_7[4] = 1
    if addr_7_bit_4 == 1:
        if np.all(data_2d[8:23] == 0):
            print("addr_8 ~ addr_22: Pass")
        else:
            print("addr_8 ~ addr_22: Error")
    else:
        print("addr_7_bit_4 == 0")
        

    # Check addr_243 ~ addr_642 if addr_7[5] = 1
    if addr_7_bit_5 == 1:
        if np.all(data_2d[243:643] == 0):
            print("addr_243 ~ addr_642: Pass")
        else:
            print("addr_243 ~ addr_642: Error")
    else:
        print("addr_7_bit_5 == 0")


# Don’t care addr_(8+N*3)[7:0] if addr_(143+N*20)=0
# Don’t care addr_(8+N*3) [7:4] if addr_(144+N*20)=0

    for N in range(5):
        # Check addr_(8+N*3)
        if np.all(data_2d[143+N*20] == 0):
            if not np.all(data_2d[8+N*3, :] == data_2d[7+N*3, -1]):
                print(f"Error: addr_{8+N*3} 1")
        if np.all(data_2d[144+N*20] == 0):
            if not np.all(data_2d[8+N*3, 4:] == data_2d[8+N*3, 3]):
                print(f"Error: addr_{8+N*3} 2")
        if np.all(data_2d[145+N*20] == 0):
            if not np.all(data_2d[8+N*3, :4] == data_2d[7+N*3, -1]):
                print(f"Error: addr_{8+N*3} 3")

        # Check addr_(9+N*3)
        if np.all(data_2d[143+N*20] == 0):
            if not np.all(data_2d[9+N*3, 4:] == data_2d[8+N*3, -1]):
                print(f"Error: addr_{9+N*3} 4")
        if np.all(data_2d[146+N*20] == 0):
            if not np.all(data_2d[9+N*3, 4:] == data_2d[9+N*3, 3]):
                print(f"Error: addr_{9+N*3} 5")
        if np.all(data_2d[153+N*20] == 0):
            if not np.all(data_2d[9+N*3, :4] == data_2d[9+N*3, 3]):
                print(f"Error: addr_{9+N*3} 6")
        if np.all(data_2d[154+N*20] == 0):
            if not np.all(data_2d[9+N*3, :4] == data_2d[9+N*3, 3]):
                print(f"Error: addr_{9+N*3} 7")

        # Check addr_(10+N*3)
        if np.all(data_2d[153+N*20] == 0):
            if not np.all(data_2d[10+N*3, :] == data_2d[9+N*3, -1]):
                print(f"Error: addr_{10+N*3} 8")
        if np.all(data_2d[155+N*20] == 0):
            if not np.all(data_2d[10+N*3, 4:] == data_2d[10+N*3, 3]):
                print(f"Error: addr_{10+N*3} 9")
        if np.all(data_2d[156+N*20] == 0):
            if not np.all(data_2d[10+N*3, :4] == data_2d[10+N*3, 3]):
                print(f"Error: addr_{10+N*3} 10")



    # addr_23 ~ addr_52, N=0~9:
    # Loop through each byte
    for N in range(10):
        # Check addr_(23+N*3)
        if np.all(data_2d[243+N*10] == 0) or np.all(data_2d[244+N*10] == 0):
            if data_2d[23+N*3, 7] != data_2d[22+N*3, -1] or data_2d[23+N*3, 3] != data_2d[23+N*3, 2]:
                print(f"Error: addr_{23+N*3} 1")

        # Check addr_(24+N*3)
        if np.all(data_2d[243+N*10] == 0) or np.all(data_2d[245+N*10] == 0):
            if data_2d[24+N*3, 7] != data_2d[23+N*3, -1] or data_2d[24+N*3, 3] != data_2d[24+N*3, 2]:
                print(f"Error: addr_{24+N*3} 2")

        # Check addr_(25+N*3)
        if np.all(data_2d[243+N*10] == 0) or np.all(data_2d[246+N*10] == 0):
            if data_2d[25+N*3, 7] != data_2d[24+N*3, -1] or data_2d[25+N*3, 3] != data_2d[25+N*3, 2]:
                print(f"Error: addr_{25+N*3} 3")
                
                
    # addr_53 ~ addr_82, N=0~9:
    # Loop through each byte
    for N in range(10):
        # Check addr_(53+N*3)
        if np.all(data_2d[343+N*10] == 0) or np.all(data_2d[344+N*10] == 0):
            if data_2d[53+N*3, 7] != data_2d[52+N*3, -1] or data_2d[53+N*3, 3] != data_2d[53+N*3, 2]:
                print(f"Error: addr_{53+N*3} 1")

        # Check addr_(54+N*3)
        if np.all(data_2d[343+N*10] == 0) or np.all(data_2d[345+N*10] == 0):
            if data_2d[54+N*3, 7] != data_2d[53+N*3, -1] or data_2d[54+N*3, 3] != data_2d[54+N*3, 2]:
                print(f"Error: addr_{54+N*3} 2")

        # Check addr_(55+N*3)
        if np.all(data_2d[343+N*10] == 0) or np.all(data_2d[346+N*10] == 0):
            if data_2d[55+N*3, 7] != data_2d[54+N*3, -1] or data_2d[55+N*3, 3] != data_2d[55+N*3, 2]:
                print(f"Error: addr_{55+N*3} 3")
                
    # addr_83 ~ addr_112, N=0~9:
    # Loop through each byte
    for N in range(10):
        # Check addr_(83+N*3)
        if np.all(data_2d[443+N*10] == 0) or np.all(data_2d[444+N*10] == 0):
            if data_2d[83+N*3, 7] != data_2d[82+N*3, -1] or data_2d[83+N*3, 3] != data_2d[83+N*3, 2]:
                print(f"Error: addr_{83+N*3} 1")

        # Check addr_(84+N*3)
        if np.all(data_2d[443+N*10] == 0) or np.all(data_2d[445+N*10] == 0):
            if data_2d[84+N*3, 7] != data_2d[83+N*3, -1] or data_2d[84+N*3, 3] != data_2d[84+N*3, 2]:
                print(f"Error: addr_{84+N*3} 2")

        # Check addr_(85+N*3)
        if np.all(data_2d[443+N*10] == 0) or np.all(data_2d[446+N*10] == 0):
            if data_2d[85+N*3, 7] != data_2d[84+N*3, -1] or data_2d[85+N*3, 3] != data_2d[85+N*3, 2]:
                print(f"Error: addr_{85+N*3} 3")

    # addr_113 ~ addr_142
    # Loop through each byte
    for N in range(10):
        # Check addr_(113+N*3)
        if np.all(data_2d[543+N*10] == 0) or np.all(data_2d[544+N*10] == 0):
            if data_2d[113+N*3, 7] != data_2d[112+N*3, -1] or data_2d[113+N*3, 3] != data_2d[113+N*3, 2]:
                print(f"Error: addr_{113+N*3} 1")

        # Check addr_(114+N*3)
        if np.all(data_2d[543+N*10] == 0) or np.all(data_2d[545+N*10] == 0):
            if data_2d[114+N*3, 7] != data_2d[113+N*3, -1] or data_2d[114+N*3, 3] != data_2d[114+N*3, 2]:
                print(f"Error: addr_{114+N*3} 2")

        # Check addr_(115+N*3)
        if np.all(data_2d[543+N*10] == 0) or np.all(data_2d[546+N*10] == 0):
            if data_2d[115+N*3, 7] != data_2d[114+N*3, -1] or data_2d[115+N*3, 3] != data_2d[115+N*3, 2]:
                print(f"Error: addr_{115+N*3} 3")
                
    # addr_143 ~ addr_242, 
    # Loop through each byte
    for N in range(10):
        # Check addr_(143+N*10)
        if np.all(data_2d[143+N*10] == 0):
            for i in range(144+N*10, 153+N*10):
                if np.any(data_2d[i, :] != data_2d[143+N*10, -1]):
                    print(f"Error: addr_{i}")

        # Check addr_(144+N*10)
        if np.all(data_2d[144+N*10] == 0):
            for i in range(147+N*10, 149+N*10):
                if np.any(data_2d[i, :] != data_2d[144+N*10, -1]):
                    print(f"Error: addr_{i}")

        # Check addr_(145+N*10)
        if np.all(data_2d[145+N*10] == 0):
            for i in range(149+N*10, 151+N*10):
                if np.any(data_2d[i, :] != data_2d[145+N*10, -1]):
                    print(f"Error: addr_{i}")

        # Check addr_(146+N*10)
        if np.all(data_2d[146+N*10] == 0):
            for i in range(151+N*10, 153+N*10):
                if np.any(data_2d[i, :] != data_2d[146+N*10, -1]):
                    print(f"Error: addr_{i}")


    #addr_243 ~ addr_342, 
    # Loop through each byte
    for N in range(10):
        # Check addr_(243+N*10)
        if np.all(data_2d[243+N*10] == 0):
            for i in range(244+N*10, 253+N*10):
                if np.any(data_2d[i, :] != data_2d[243+N*10, -1]):
                    print(f"Error: addr_{i}")

        # Check addr_(244+N*10)
        if np.all(data_2d[244+N*10] == 0):
            for i in range(247+N*10, 249+N*10):
                if np.any(data_2d[i, :] != data_2d[244+N*10, -1]):
                    print(f"Error: addr_{i}")

        # Check addr_(245+N*10)
        if np.all(data_2d[245+N*10] == 0):
            for i in range(249+N*10, 251+N*10):
                if np.any(data_2d[i, :] != data_2d[245+N*10, -1]):
                    print(f"Error: addr_{i}")

        # Check addr_(246+N*10)
        if np.all(data_2d[246+N*10] == 0):
            for i in range(251+N*10, 253+N*10):
                if np.any(data_2d[i, :] != data_2d[246+N*10, -1]):
                    print(f"Error: addr_{i}")


    # addr_343 ~ addr_442
    # Loop through each byte
    for N in range(10):
        # Check addr_(343+N*10)
        if np.all(data_2d[343+N*10] == 0):
            for i in range(344+N*10, 353+N*10):
                if np.any(data_2d[i, :] != data_2d[343+N*10, -1]):
                    print(f"Error: addr_{i}")

        # Check addr_(344+N*10)
        if np.all(data_2d[344+N*10] == 0):
            for i in range(347+N*10, 349+N*10):
                if np.any(data_2d[i, :] != data_2d[344+N*10, -1]):
                    print(f"Error: addr_{i}")

        # Check addr_(345+N*10)
        if np.all(data_2d[345+N*10] == 0):
            for i in range(349+N*10, 351+N*10):
                if np.any(data_2d[i, :] != data_2d[345+N*10, -1]):
                    print(f"Error: addr_{i}")

        # Check addr_(346+N*10)
        if np.all(data_2d[346+N*10] == 0):
            for i in range(351+N*10, 353+N*10):
                if np.any(data_2d[i, :] != data_2d[346+N*10, -1]):
                    print(f"Error: addr_{i}")

    # addr_443 ~ addr_542, N=0~9:
    # Iterate over each byte
    for N in range(10):
        # If addr_(443+N*10) equals 0
        if np.all(data_2d[443+N*10] == 0):
            for i in range(444+N*10, 453+N*10):
                if data_2d[i] != data_2d[442+N*10][-1]:
                    print(f"Error: addr_{i} does not match last bit of addr_{442+N*10}")

        # If addr_(444+N*10) equals 0
        if np.all(data_2d[444+N*10] == 0):
            for i in range(447+N*10, 449+N*10):
                if data_2d[i] != data_2d[443+N*10][-1]:
                    print(f"Error: addr_{i} does not match last bit of addr_{443+N*10}")

        # If addr_(445+N*10) equals 0
        if np.all(data_2d[445+N*10] == 0):
            for i in range(449+N*10, 451+N*10):
                if data_2d[i] != data_2d[444+N*10][-1]:
                    print(f"Error: addr_{i} does not match last bit of addr_{444+N*10}")

        # If addr_(446+N*10) equals 0
        if np.all(data_2d[446+N*10] == 0):
            for i in range(451+N*10, 453+N*10):
                if data_2d[i] != data_2d[445+N*10][-1]:
                    print(f"Error: addr_{i} does not match last bit of addr_{445+N*10}")


    # addr_543 ~ addr_642, N=0~9:
    # Iterate over each byte
    for N in range(10):
        # If addr_(543+N*10) equals 0
        if np.all(data_2d[543+N*10] == 0):
            for i in range(544+N*10, 553+N*10):
                if data_2d[i] != data_2d[542+N*10][-1]:
                    print(f"Error: addr_{i} does not match last bit of addr_{542+N*10}")


        # If addr_(544+N*10) equals 0
        if np.all(data_2d[544+N*10] == 0):
            for i in range(547+N*10, 549+N*10):
                if data_2d[i] != data_2d[543+N*10][-1]:
                    print(f"Error: addr_{i} does not match last bit of addr_{543+N*10}")

        # If addr_(545+N*10) equals 0
        if np.all(data_2d[545+N*10] == 0):
            for i in range(549+N*10, 551+N*10):
                if data_2d[i] != data_2d[544+N*10][-1]:
                    print(f"Error: addr_{i} does not match last bit of addr_{544+N*10}")

        # If addr_(546+N*10) equals 0
        if np.all(data_2d[546+N*10] == 0):
            for i in range(551+N*10, 553+N*10):
                if data_2d[i] != data_2d[545+N*10][-1]:
                    print(f"Error: addr_{i} does not match last bit of addr_{545+N*10}")


def check_care(processed_file, original_file):
    # Open the files
    with open(processed_file, "r") as p_file:
        pbits = p_file.read().strip()
    
    with open(original_file, "r") as o_file:
        obits = o_file.read().strip()

    # Check if total bits is a multiple of 8
    if len(pbits) % 8 != 0:
        raise ValueError(f"Total number of pbits should be a multiple of 8, but got {len(pbits)} bits")
    
    if len(obits) % 8 != 0:
        raise ValueError(f"Total number of obits should be a multiple of 8, but got {len(obits)} bits")

    # Initialize lists to store 8-bit chunks
    origin_data = []
    process_data = []

    # Read every 8 bits
    for i in range(0, len(pbits), 8):
        # Convert the 8-bit binary number to a list of ints
        process_data.append([int(bit) for bit in pbits[i:i+8]])

    for i in range(0, len(obits), 8):
        # Convert the 8-bit binary number to a list of ints
        origin_data.append([int(bit) for bit in obits[i:i+8]])

    # Convert to 2D NumPy array
    # Convert to 2D NumPy array
    process_data = np.array(process_data)
    origin_data = np.array(origin_data)


    


    #reverse
    process_data = process_data[:, ::-1]
    origin_data = origin_data[:, ::-1]




    #addr 7 0~3
    process_data[7, :4] = 0
    origin_data[7, :4] = 0

    if origin_data[7, 4] == 1:
        origin_data[8:23, :] = 0
        process_data[8:23, :] = 0
    
    if origin_data[7, 5] == 1:
        origin_data[243:642, :] = 0
        process_data[243:642, :] = 0




    for N in range(5):  # N=0~4
        if np.all(origin_data[143+N*20, :] == 0):
            origin_data[8+N*3, :] = 0
            process_data[8+N*3, :] = 0

        if np.all(origin_data[144+N*20, :] == 0):
            origin_data[8+N*3, 4:] = 0
            process_data[8+N*3, 4:] = 0

        if np.all(origin_data[145+N*20, :] == 0):
            origin_data[8+N*3, :4] = 0
            process_data[8+N*3, :4] = 0

        if np.all(origin_data[143+N*20, :] == 0):
            origin_data[9+N*3, 4:] = 0
            process_data[9+N*3, 4:] = 0

        if np.all(origin_data[146+N*20, :] == 0):
            origin_data[9+N*3, 4:] = 0
            process_data[9+N*3, 4:] = 0

        if np.all(origin_data[153+N*20, :] == 0) or np.all(origin_data[154+N*20, :] == 0):
            origin_data[9+N*3, :4] = 0
            process_data[9+N*3, :4] = 0

        if np.all(origin_data[153+N*20, :] == 0):
            origin_data[10+N*3, :] = 0
            process_data[10+N*3, :] = 0

        if np.all(origin_data[155+N*20, :] == 0):
            origin_data[10+N*3, 4:] = 0
            process_data[10+N*3, 4:] = 0

        if np.all(origin_data[156+N*20, :] == 0):
            origin_data[10+N*3, :4] = 0
            process_data[10+N*3, :4] = 0



            # for addr_23 ~ addr_52
    for N in range(10):  # N=0~9
        # For all conditions, bit7 & bit3 should not be cared for
        origin_data[23+N*3, [7,3]] = 0
        origin_data[24+N*3, [7,3]] = 0
        origin_data[25+N*3, [7,3]] = 0
        process_data[23+N*3, [7,3]] = 0
        process_data[24+N*3, [7,3]] = 0
        process_data[25+N*3, [7,3]] = 0

        # If either addr_(243+N*10) or addr_(244+N*10) are all 0, don't care the whole byte
        if np.all(origin_data[243+N*10, :] == 0) or np.all(origin_data[244+N*10, :] == 0):
            origin_data[23+N*3, :] = 0
            process_data[23+N*3, :] = 0

        # If either addr_(243+N*10) or addr_(245+N*10) are all 0, don't care the whole byte
        if np.all(origin_data[243+N*10, :] == 0) or np.all(origin_data[245+N*10, :] == 0):
            origin_data[24+N*3, :] = 0
            process_data[24+N*3, :] = 0

        # If either addr_(243+N*10) or addr_(246+N*10) are all 0, don't care the whole byte
        if np.all(origin_data[243+N*10, :] == 0) or np.all(origin_data[246+N*10, :] == 0):
            origin_data[25+N*3, :] = 0
            process_data[25+N*3, :] = 0

        # Repeat for addr_53 ~ addr_82, just update the range for origin_data
    for N in range(10):  # N=0~9
        # For all conditions, bit7 & bit3 should not be cared for
        origin_data[53+N*3, [7,3]] = 0
        origin_data[54+N*3, [7,3]] = 0
        origin_data[55+N*3, [7,3]] = 0
        process_data[53+N*3, [7,3]] = 0
        process_data[54+N*3, [7,3]] = 0
        process_data[55+N*3, [7,3]] = 0

        # If either addr_(343+N*10) or addr_(344+N*10) are all 0, don't care the whole byte
        if np.all(origin_data[343+N*10, :] == 0) or np.all(origin_data[344+N*10, :] == 0):
            origin_data[53+N*3, :] = 0
            process_data[53+N*3, :] = 0

        # If either addr_(343+N*10) or addr_(345+N*10) are all 0, don't care the whole byte
        if np.all(origin_data[343+N*10, :] == 0) or np.all(origin_data[345+N*10, :] == 0):
            origin_data[54+N*3, :] = 0
            process_data[54+N*3, :] = 0

        # If either addr_(343+N*10) or addr_(346+N*10) are all 0, don't care the whole byte
        if np.all(origin_data[343+N*10, :] == 0) or np.all(origin_data[346+N*10, :] == 0):
            origin_data[55+N*3, :] = 0
            process_data[55+N*3, :] = 0

    # addr_83 ~ addr_112
    addr_base = 83
    origin_data_base = 443
    for N in range(10):  # N=0~9
        # For all conditions, bit7 & bit3 should not be cared for
        origin_data[addr_base+N*3, [7,3]] = 0
        process_data[addr_base+N*3, [7,3]] = 0

        origin_data[addr_base+1+N*3, [7,3]] = 0
        process_data[addr_base+1+N*3, [7,3]] = 0

        origin_data[addr_base+2+N*3, [7,3]] = 0
        process_data[addr_base+2+N*3, [7,3]] = 0

        # Check conditions for addr_(addr_base+N*3)
        if np.all(origin_data[origin_data_base+N*10, :] == 0) or np.all(origin_data[origin_data_base+1+N*10, :] == 0):
            origin_data[addr_base+N*3, :] = 0
            process_data[addr_base+N*3, :] = 0

        # Check conditions for addr_(addr_base+1+N*3)
        if np.all(origin_data[origin_data_base+N*10, :] == 0) or np.all(origin_data[origin_data_base+2+N*10, :] == 0):
            origin_data[addr_base+1+N*3, :] = 0
            process_data[addr_base+1+N*3, :] = 0

        # Check conditions for addr_(addr_base+2+N*3)
        if np.all(origin_data[origin_data_base+N*10, :] == 0) or np.all(origin_data[origin_data_base+3+N*10, :] == 0):
            origin_data[addr_base+2+N*3, :] = 0
            process_data[addr_base+2+N*3, :] = 0

    # addr_83 ~ addr_112
    addr_base = 83
    origin_data_base = 443
    for N in range(10):  # N=0~9
        # For all conditions, bit7 & bit3 should not be cared for
        origin_data[addr_base+N*3, [7,3]] = 0
        process_data[addr_base+N*3, [7,3]] = 0

        origin_data[addr_base+1+N*3, [7,3]] = 0
        process_data[addr_base+1+N*3, [7,3]] = 0

        origin_data[addr_base+2+N*3, [7,3]] = 0
        process_data[addr_base+2+N*3, [7,3]] = 0

        # Check conditions for addr_(addr_base+N*3)
        if np.all(origin_data[origin_data_base+N*10, :] == 0) or np.all(origin_data[origin_data_base+1+N*10, :] == 0):
            origin_data[addr_base+N*3, :] = 0
            process_data[addr_base+N*3, :] = 0

        # Check conditions for addr_(addr_base+1+N*3)
        if np.all(origin_data[origin_data_base+N*10, :] == 0) or np.all(origin_data[origin_data_base+2+N*10, :] == 0):
            origin_data[addr_base+1+N*3, :] = 0
            process_data[addr_base+1+N*3, :] = 0

        # Check conditions for addr_(addr_base+2+N*3)
        if np.all(origin_data[origin_data_base+N*10, :] == 0) or np.all(origin_data[origin_data_base+3+N*10, :] == 0):
            origin_data[addr_base+2+N*3, :] = 0
            process_data[addr_base+2+N*3, :] = 0
        

    # addr_113 ~ addr_142
    addr_base = 113
    origin_data_base = 543
    for N in range(10):  # N=0~9
        # For all conditions, bit7 & bit3 should not be cared for
        origin_data[addr_base+N*3, [7,3]] = 0
        process_data[addr_base+N*3, [7,3]] = 0

        origin_data[addr_base+1+N*3, [7,3]] = 0
        process_data[addr_base+1+N*3, [7,3]] = 0

        origin_data[addr_base+2+N*3, [7,3]] = 0
        process_data[addr_base+2+N*3, [7,3]] = 0

        # Check conditions for addr_(addr_base+N*3)
        if np.all(origin_data[origin_data_base+N*10, :] == 0) or np.all(origin_data[origin_data_base+1+N*10, :] == 0):
            origin_data[addr_base+N*3, :] = 0
            process_data[addr_base+N*3, :] = 0

        # Check conditions for addr_(addr_base+1+N*3)
        if np.all(origin_data[origin_data_base+N*10, :] == 0) or np.all(origin_data[origin_data_base+2+N*10, :] == 0):
            origin_data[addr_base+1+N*3, :] = 0
            process_data[addr_base+1+N*3, :] = 0

        # Check conditions for addr_(addr_base+2+N*3)
        if np.all(origin_data[origin_data_base+N*10, :] == 0) or np.all(origin_data[origin_data_base+3+N*10, :] == 0):
            origin_data[addr_base+2+N*3, :] = 0
            process_data[addr_base+2+N*3, :] = 0
    



    # addr_143 ~ addr_242
    addr_base = 143
    for N in range(10):  # N=0~9
        # If addr_(143+N*10)=0  Don’t care addr_(144+N*10) ~ addr_(152+N*10) 9 bytes
        if np.all(origin_data[addr_base+N*10, :] == 0):
            origin_data[addr_base+1+N*10:addr_base+10+N*10, :] = 0
            process_data[addr_base+1+N*10:addr_base+10+N*10, :] = 0

        # If addr_(144+N*10)=0  Don’t care addr_(147+N*10) & addr_(148+N*10) 2 bytes
        if np.all(origin_data[addr_base+1+N*10, :] == 0):
            origin_data[addr_base+4+N*10:addr_base+6+N*10, :] = 0
            process_data[addr_base+4+N*10:addr_base+6+N*10, :] = 0

        # If addr_(145+N*10)=0  Don’t care addr_(149+N*10) & addr_(150+N*10) 2 bytes
        if np.all(origin_data[addr_base+2+N*10, :] == 0):
            origin_data[addr_base+6+N*10:addr_base+8+N*10, :] = 0
            process_data[addr_base+6+N*10:addr_base+8+N*10, :] = 0

        # If addr_(146+N*10)=0  Don’t care addr_(151+N*10) & addr_(152+N*10) 2 bytes
        if np.all(origin_data[addr_base+3+N*10, :] == 0):
            origin_data[addr_base+8+N*10:addr_base+10+N*10, :] = 0
            process_data[addr_base+8+N*10:addr_base+10+N*10, :] = 0

    # addr_243 ~ addr_342
    addr_base = 243
    for N in range(10):  # N=0~9
        # If addr_(243+N*10)=0  Don’t care addr_(244+N*10) ~ addr_(252+N*10) 9 bytes
        if np.all(origin_data[addr_base+N*10, :] == 0):
            origin_data[addr_base+1+N*10:addr_base+10+N*10, :] = 0
            process_data[addr_base+1+N*10:addr_base+10+N*10, :] = 0

        # If addr_(244+N*10)=0  Don’t care addr_(247+N*10) & addr_(248+N*10) 2 bytes
        if np.all(origin_data[addr_base+1+N*10, :] == 0):
            origin_data[addr_base+4+N*10:addr_base+6+N*10, :] = 0
            process_data[addr_base+4+N*10:addr_base+6+N*10, :] = 0

        # If addr_(245+N*10)=0  Don’t care addr_(249+N*10) & addr_(250+N*10) 2 bytes
        if np.all(origin_data[addr_base+2+N*10, :] == 0):
            origin_data[addr_base+6+N*10:addr_base+8+N*10, :] = 0
            process_data[addr_base+6+N*10:addr_base+8+N*10, :] = 0

        # If addr_(246+N*10)=0  Don’t care addr_(251+N*10) & addr_(252+N*10) 2 bytes
        if np.all(origin_data[addr_base+3+N*10, :] == 0):
            origin_data[addr_base+8+N*10:addr_base+10+N*10, :] = 0
            process_data[addr_base+8+N*10:addr_base+10+N*10, :] = 0
    # addr_343 ~ addr_442
    addr_base = 343
    for N in range(10):  # N=0~9
        # If addr_(343+N*10)=0  Don’t care addr_(344+N*10) ~ addr_(352+N*10) 9 bytes
        if np.all(origin_data[addr_base+N*10, :] == 0):
            origin_data[addr_base+1+N*10:addr_base+10+N*10, :] = 0
            process_data[addr_base+1+N*10:addr_base+10+N*10, :] = 0

        # If addr_(344+N*10)=0  Don’t care addr_(347+N*10) & addr_(348+N*10) 2 bytes
        if np.all(origin_data[addr_base+1+N*10, :] == 0):
            origin_data[addr_base+4+N*10:addr_base+6+N*10, :] = 0
            process_data[addr_base+4+N*10:addr_base+6+N*10, :] = 0

        # If addr_(345+N*10)=0  Don’t care addr_(349+N*10) & addr_(350+N*10) 2 bytes
        if np.all(origin_data[addr_base+2+N*10, :] == 0):
            origin_data[addr_base+6+N*10:addr_base+8+N*10, :] = 0
            process_data[addr_base+6+N*10:addr_base+8+N*10, :] = 0

        # If addr_(346+N*10)=0  Don’t care addr_(351+N*10) & addr_(352+N*10) 2 bytes
        if np.all(origin_data[addr_base+3+N*10, :] == 0):
            origin_data[addr_base+8+N*10:addr_base+10+N*10, :] = 0
            process_data[addr_base+8+N*10:addr_base+10+N*10, :] = 0

    # addr_443 ~ addr_542
    addr_base = 443
    for N in range(10):  # N=0~9
        # If addr_(443+N*10)=0  Don’t care addr_(444+N*10) ~ addr_(452+N*10) 9 bytes
        if np.all(origin_data[addr_base+N*10, :] == 0):
            origin_data[addr_base+1+N*10:addr_base+10+N*10, :] = 0
            process_data[addr_base+1+N*10:addr_base+10+N*10, :] = 0

        # If addr_(444+N*10)=0  Don’t care addr_(447+N*10) & addr_(448+N*10) 2 bytes
        if np.all(origin_data[addr_base+1+N*10, :] == 0):
            origin_data[addr_base+4+N*10:addr_base+6+N*10, :] = 0
            process_data[addr_base+4+N*10:addr_base+6+N*10, :] = 0

        # If addr_(445+N*10)=0  Don’t care addr_(449+N*10) & addr_(450+N*10) 2 bytes
        if np.all(origin_data[addr_base+2+N*10, :] == 0):
            origin_data[addr_base+6+N*10:addr_base+8+N*10, :] = 0
            process_data[addr_base+6+N*10:addr_base+8+N*10, :] = 0

        # If addr_(446+N*10)=0  Don’t care addr_(451+N*10) & addr_(452+N*10) 2 bytes
        if np.all(origin_data[addr_base+3+N*10, :] == 0):
            origin_data[addr_base+8+N*10:addr_base+10+N*10, :] = 0
            process_data[addr_base+8+N*10:addr_base+10+N*10, :] = 0

    # addr_543 ~ addr_642
    addr_base = 543
    for N in range(10):  # N=0~9
        # If addr_(543+N*10)=0  Don’t care addr_(544+N*10) ~ addr_(552+N*10) 9 bytes
        if np.all(origin_data[addr_base+N*10, :] == 0):
            origin_data[addr_base+1+N*10:addr_base+10+N*10, :] = 0
            process_data[addr_base+1+N*10:addr_base+10+N*10, :] = 0

        # If addr_(544+N*10)=0  Don’t care addr_(547+N*10) & addr_(548+N*10) 2 bytes
        if np.all(origin_data[addr_base+1+N*10, :] == 0):
            origin_data[addr_base+4+N*10:addr_base+6+N*10, :] = 0
            process_data[addr_base+4+N*10:addr_base+6+N*10, :] = 0

        # If addr_(545+N*10)=0  Don’t care addr_(549+N*10) & addr_(550+N*10) 2 bytes
        if np.all(origin_data[addr_base+2+N*10, :] == 0):
            origin_data[addr_base+6+N*10:addr_base+8+N*10, :] = 0
            process_data[addr_base+6+N*10:addr_base+8+N*10, :] = 0

        # If addr_(546+N*10)=0  Don’t care addr_(551+N*10) & addr_(552+N*10) 2 bytes
        if np.all(origin_data[addr_base+3+N*10, :] == 0):
            origin_data[addr_base+8+N*10:addr_base+10+N*10, :] = 0
            process_data[addr_base+8+N*10:addr_base+10+N*10, :] = 0

    


if __name__ == '__main__':
    arr = file2arr()
    # check_dont_care(arr)
