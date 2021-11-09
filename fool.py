compare_string = "TamilCTF{StRiNgs_C0mP4re5}"
def find_me(par):
    flag = [0] * 26
    flag[0] = par[0] >> 2
    flag[1] = par[2] ^ 0x1f
    flag[2] = (par[1] * 2) ^ 0xb
    flag[3] = (par[3] - 0xb) ^ 0x15
    flag[4] = (par[6] * 3) // 2
    flag[5] = par[4] - 0xf
    flag[6] = (par[5] ^ 2) - 0x45
    flag[7] = par[7] ^ 0x29
    flag[8] = (par[9] * 2) - 7
    flag[9] = 196 - (par[8] * 2)
    flag[10] = par[12] << 4
    flag[11] = par[10] - 5
    flag[12] = par[11] + 0x16
    flag[13] = par[14]
    flag[14] = par[16] + 0x3d
    flag[15] = par[15] ^ 0x23
    flag[16] = (par[17] * 12) >> 0x3
    flag[17] = par[19] << 0x1
    flag[18] = par[18] - 0x1d
    flag[19] = (par[21] * 2) // 4
    flag[20] = par[20] ^ 0x46
    flag[21] = (par[13] ^ 0x2d) << 2
    flag[22] = par[23] ^ 0xd
    flag[23] = (par[24] ^ 1) + 0x1d
    flag[24] = par[22] // 2
    flag[25] = par[25] ^ 0x42
    print (''.join([chr(i) for i in flag]))

find_me(compare_string)