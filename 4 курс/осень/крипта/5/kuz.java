package ucheba.kuznechik;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.binary.Hex;

public class Main {
    static final int BLOCK_SIZE = 16; // длина блока в байтах

    static final byte[] Pi = {
            (byte) 0xFC, (byte) 0xEE, (byte) 0xDD, 0x11, (byte) 0xCF, 0x6E, 0x31, 0x16,
            (byte) 0xFB, (byte) 0xC4, (byte) 0xFA, (byte) 0xDA, 0x23, (byte) 0xC5, 0x04, 0x4D,
            (byte) 0xE9, 0x77, (byte) 0xF0, (byte) 0xDB, (byte) 0x93, 0x2E, (byte) 0x99, (byte) 0xBA,
            0x17, 0x36, (byte) 0xF1, (byte) 0xBB, 0x14, (byte) 0xCD, 0x5F, (byte) 0xC1,
            (byte) 0xF9, 0x18, 0x65, 0x5A, (byte) 0xE2, 0x5C, (byte) 0xEF, 0x21,
            (byte) 0x81, 0x1C, 0x3C, 0x42, (byte) 0x8B, 0x01, (byte) 0x8E, 0x4F,
            0x05, (byte) 0x84, 0x02, (byte) 0xAE, (byte) 0xE3, 0x6A, (byte) 0x8F, (byte) 0xA0,
            0x06, 0x0B, (byte) 0xED, (byte) 0x98, 0x7F, (byte) 0xD4, (byte) 0xD3, 0x1F,
            (byte) 0xEB, 0x34, 0x2C, 0x51, (byte) 0xEA, (byte) 0xC8, 0x48, (byte) 0xAB,
            (byte) 0xF2, 0x2A, 0x68, (byte) 0xA2, (byte) 0xFD, 0x3A, (byte) 0xCE, (byte) 0xCC,
            (byte) 0xB5, 0x70, 0x0E, 0x56, 0x08, 0x0C, 0x76, 0x12,
            (byte) 0xBF, 0x72, 0x13, 0x47, (byte) 0x9C, (byte) 0xB7, 0x5D, (byte) 0x87,
            0x15, (byte) 0xA1, (byte) 0x96, 0x29, 0x10, 0x7B, (byte) 0x9A, (byte) 0xC7,
            (byte) 0xF3, (byte) 0x91, 0x78, 0x6F, (byte) 0x9D, (byte) 0x9E, (byte) 0xB2, (byte) 0xB1,
            0x32, 0x75, 0x19, 0x3D, (byte) 0xFF, 0x35, (byte) 0x8A, 0x7E,
            0x6D, 0x54, (byte) 0xC6, (byte) 0x80, (byte) 0xC3, (byte) 0xBD, 0x0D, 0x57,
            (byte) 0xDF, (byte) 0xF5, 0x24, (byte) 0xA9, 0x3E, (byte) 0xA8, (byte) 0x43, (byte) 0xC9,
            (byte) 0xD7, 0x79, (byte) 0xD6, (byte) 0xF6, 0x7C, 0x22, (byte) 0xB9, 0x03,
            (byte) 0xE0, 0x0F, (byte) 0xEC, (byte) 0xDE, 0x7A, (byte) 0x94, (byte) 0xB0, (byte) 0xBC,
            (byte) 0xDC, (byte) 0xE8, 0x28, 0x50, 0x4E, 0x33, 0x0A, 0x4A,
            (byte) 0xA7, (byte) 0x97, 0x60, 0x73, 0x1E, 0x00, 0x62, 0x44,
            0x1A, (byte) 0xB8, 0x38, (byte) 0x82, 0x64, (byte) 0x9F, 0x26, 0x41,
            (byte) 0xAD, 0x45, 0x46, (byte) 0x92, 0x27, 0x5E, 0x55, 0x2F,
            (byte) 0x8C, (byte) 0xA3, (byte) 0xA5, 0x7D, 0x69, (byte) 0xD5, (byte) 0x95, 0x3B,
            0x07, 0x58, (byte) 0xB3, 0x40, (byte) 0x86, (byte) 0xAC, 0x1D, (byte) 0xF7,
            0x30, 0x37, 0x6B, (byte) 0xE4, (byte) 0x88, (byte) 0xD9, (byte) 0xE7, (byte) 0x89,
            (byte) 0xE1, 0x1B, (byte) 0x83, 0x49, 0x4C, 0x3F, (byte) 0xF8, (byte) 0xFE,
            (byte) 0x8D, 0x53, (byte) 0xAA, (byte) 0x90, (byte) 0xCA, (byte) 0xD8, (byte) 0x85, 0x61,
            0x20, 0x71, 0x67, (byte) 0xA4, 0x2D, 0x2B, 0x09, 0x5B,
            (byte) 0xCB, (byte) 0x9B, 0x25, (byte) 0xD0, (byte) 0xBE, (byte) 0xE5, 0x6C, 0x52,
            0x59, (byte) 0xA6, 0x74, (byte) 0xD2, (byte) 0xE6, (byte) 0xF4, (byte) 0xB4, (byte) 0xC0,
            (byte) 0xD1, 0x66, (byte) 0xAF, (byte) 0xC2, 0x39, 0x4B, 0x63, (byte) 0xB6
    };

    // вектор линейного преобразования
    static final byte[] l_vec = {
            1, (byte) 148, 32, (byte) 133, 16, (byte) 194, (byte) 192, 1,
            (byte) 251, 1, (byte) 192, (byte) 194, 16, (byte) 133, 32, (byte) 148
    };

    // массив для хранения констант
    static byte[][] iteration_C = new byte[32][16];

    // массив для хранения ключей
    static byte[][] iteration_key = new byte[10][64];

    static private byte[] Round_Kuz_X(byte[] a, byte[] b)
    {
        int i;
        byte[] c = new byte[BLOCK_SIZE];
        for (i = 0; i < BLOCK_SIZE; i++)
            c[i] = (byte) (a[i] ^ b[i]);
        return c;
    }

    // Функция S
    static private byte[] Round_Kuz_S(byte[] in_data)
    {
        int i;
        byte[] out_data = new byte[in_data.length];
        for (i = 0; i < BLOCK_SIZE; i++)
        {
            int data = in_data[i];
            if(data < 0)
            {
                data = data + 256;
            }
            out_data[i] = Pi[data];
        }
        return out_data;
    }

    static private byte Round_Kuz_GF_mul(byte a, byte b)
    {
        byte c = 0;
        byte hi_bit;
        int i;
        for (i = 0; i < 8; i++)
        {
            if ((b & 1) == 1)
                c ^= a;
            hi_bit = (byte) (a & 0x80);
            a <<= 1;
            if (hi_bit < 0)
                a ^= (byte) 0xc3; //полином  x^8+x^7+x^6+x+1
            b >>= 1;
        }
        return c;
    }
    // функция R сдвигает данные и реализует уравнение, представленное для расчета L-функции
    static private byte[] Round_Kuz_R(byte[] state)
    {
        int i;
        byte a_15 = 0;
        byte[] internal = new byte[16];
        for (i = 15; i >= 0; i--)
        {
            if(i == 0)
                internal[15] = state[i];
            else
                internal[i - 1] = state[i];
            a_15 ^= Round_Kuz_GF_mul(state[i], l_vec[i]);
        }
        internal[15] = a_15;
        return internal;
    }

    static private byte[]  Round_Kuz_L(byte[] in_data)
    {
        int i;
        byte[] out_data;
        byte[] internal = in_data;
        for (i = 0; i < 16; i++)
        {
            internal = Round_Kuz_R(internal);

        }
        out_data = internal;
        return out_data;
    }

    static private void Round_Kuz_Get_C()
    {
        int i;
        byte[][] iteration_num = new byte[32][16];
        for (i = 0; i < 32; i++)
        {
            for(int j = 0; j < BLOCK_SIZE; j++)
                iteration_num[i][j] = 0;
            iteration_num[i][0] = (byte) (i+1);
        }
        for (i = 0; i < 32; i++)
        {
            iteration_C[i] = Round_Kuz_L(iteration_num[i]);
        }
    }
    // функция, выполняющая преобразования ячейки Фейстеля
    static private byte[][] Round_Kuz_F(byte[] in_key_1, byte[] in_key_2, byte[] iteration_const, int iterationIndex)
    {
        byte[] internal;
        internal = Round_Kuz_X(in_key_1, iteration_const);
        System.out.println("\nresult after X operation in iteration "  + iterationIndex + ": " + Hex.encodeHexString(internal));
        internal = Round_Kuz_S(internal);
        System.out.println("result after S operation in iteration "  + iterationIndex + ": " + Hex.encodeHexString(internal));
        internal = Round_Kuz_L(internal);
        System.out.println("result after L operation in iteration "  + iterationIndex + ": " + Hex.encodeHexString(internal));
        byte[] out_key_1 = Round_Kuz_X(internal, in_key_2);
        System.out.println("result after xor operation in iteration "  + iterationIndex + ": " + Hex.encodeHexString(out_key_1));
        byte[][] key = new byte[2][];
        key[0] = out_key_1;
        key[1] = in_key_1;
        System.out.println("key in iteration "  + iterationIndex + ": " + Hex.encodeHexString(key[0]) + " " + Hex.encodeHexString(key[1]));
        return key;
    }
    // функция расчета раундовых ключей
    public static void GOST_Kuz_Expand_Key(byte[] key_1, byte[] key_2)
    {
        int i;

        byte[][] iteration12 = new byte[2][];
        byte[][] iteration34;
        Round_Kuz_Get_C();
        iteration_key[0] = key_1;
        iteration_key[1] = key_2;
        iteration12[0] = key_1;
        iteration12[1] = key_2;
        for (i = 0; i < 4; i++)
        {
            iteration34 = Round_Kuz_F(iteration12[0], iteration12[1], iteration_C[8 * i], 8 * i + 1);
            iteration12 = Round_Kuz_F(iteration34[0], iteration34[1], iteration_C[1 + 8 * i], 8 * i + 2);
            iteration34 = Round_Kuz_F(iteration12[0], iteration12[1], iteration_C[2 + 8 * i], 8 * i + 3);
            iteration12 = Round_Kuz_F(iteration34[0], iteration34[1], iteration_C[3 + 8 * i], 8 * i + 4);
            iteration34 = Round_Kuz_F(iteration12[0], iteration12[1], iteration_C[4 + 8 * i], 8 * i + 5);
            iteration12 = Round_Kuz_F(iteration34[0], iteration34[1], iteration_C[5 + 8 * i], 8 * i + 6);
            iteration34 = Round_Kuz_F(iteration12[0], iteration12[1], iteration_C[6 + 8 * i], 8 * i + 7);
            iteration12 = Round_Kuz_F(iteration34[0], iteration34[1], iteration_C[7 + 8 * i], 8 * i + 8);
            iteration_key[2 * i + 2] = iteration12[0];
            iteration_key[2 * i + 3] = iteration12[1];
        }

        for(i = 0; i < 10; i++)
        {
            System.out.println("key " + (i + 1) + ": " + Hex.encodeHexString(iteration_key[i]));
        }
    }
    // функция шифрования блока
    public static void GOST_Kuz_Encrypt(byte[] blk)
    {
        int i;
        byte[] out_blk;
        out_blk = blk;
        for(i = 0; i < 9; i++)
        {
            System.out.println("\nround " + (i + 1));
            out_blk = Round_Kuz_X(iteration_key[i], out_blk);
            System.out.println("result after X operation in round " + (i + 1) + ": " + Hex.encodeHexString(out_blk));
            out_blk = Round_Kuz_S(out_blk);
            System.out.println("result after S operation in round " + (i + 1) + ": " + Hex.encodeHexString(out_blk));
            out_blk = Round_Kuz_L(out_blk);
            System.out.println("result after L operation in round " + (i + 1) + ": " + Hex.encodeHexString(out_blk));
        }

        System.out.println("\nround 10");
        out_blk = Round_Kuz_X(out_blk, iteration_key[9]);

        System.out.println("result after 10 round: " + Hex.encodeHexString(out_blk));
    }
    //функция расшифрования блока

    static byte[] key_1 = {
            0x31, 0x33, 0x38, 0x34,
            0x56, 0x4C, 0x41, 0x44,
            0x49, 0x4D, 0x49, 0x52,
            0x4F, 0x56, 0x4E, 0x41,
    };
    //31 33 38 34
    // 56 4C 41 44
    // 49 4D 49 52
    // 4F 56 4E 41 31 33 38 34 56 4C 41 44 49 4D 49 52 4F 56 4E 41

    public static void main(String[] args)
    {
        byte[] blk = null;
        try {
            //blk = Hex.decodeHex("424F424B4F56564C414449534C415633".toCharArray());
            blk = Hex.decodeHex("55534143484556414441524941313233".toCharArray());
        } catch (DecoderException e) {
            System.out.println("Invalid hexadecimal string: " + e.getMessage());
        }
        assert blk != null;
        System.out.println("plain text: " + new String(blk));
        System.out.println("key: " + new String(key_1) + new String(key_1));
        System.out.println("key in hex: " + Hex.encodeHexString(key_1) + Hex.encodeHexString(key_1));
        GOST_Kuz_Expand_Key(key_1, key_1);
        GOST_Kuz_Encrypt(blk);
    }
}