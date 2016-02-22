import java.io.IOException;
import java.io.InputStream;
import java.util.BitSet;
import java.util.HashSet;
import java.util.InputMismatchException;

public class primesieve {

    static class InputReader {

        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int read() {
            if (numChars == -1)
                throw new InputMismatchException();
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }

        public String readString() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            StringBuilder res = new StringBuilder();
            do {
                if (Character.isValidCodePoint(c))
                    res.appendCodePoint(c);
                c = read();
            } while (!isSpaceChar(c));
            return res.toString();
        }

        public int readInt() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public boolean isSpaceChar(int c) {
            return this.isWhitespace(c);
        }

        public boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public char readCharacter() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            return (char) c;
        }
    }

    public static void main (String [] args) throws IOException {
        InputReader ir = new InputReader(System.in);
        int n = ir.readInt();
        int q = ir.readInt();

        int size = n / 2 + 1;
        BitSet bitSet = new BitSet(size);
        bitSet.set(0, size);
        int limit = (int) Math.sqrt(n);
        for (int i = 1; i < limit; i++) {
            if (bitSet.get(i)) {
                int val = i * 2 + 1;
                for (int j = i + val; j < size; j += val) {
                    bitSet.set(j, false);
                }
            }
        }
        int c = 0;
        for (int i = 0; i < size; i++) {
            if (bitSet.get(i)) {
                c++;
            }
        }
        System.out.println(c);
        for (int i = 0; i < q; i++) {
            int x = ir.readInt();
            if (x == 1) {
                System.out.println(0);
            } else if (x % 2 == 0) {
                System.out.println(x == 2 ? 1 : 0);
            } else {
                System.out.println(bitSet.get(x / 2) ? 1 : 0);
            }
        }
    }
}