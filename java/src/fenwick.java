import java.io.*;
import java.util.InputMismatchException;

public class fenwick {

    public static class Tree {
        private long [] tree;
        public Tree(int n) {
            tree = new long[n + 1];
        }

        public void update(int index, int v) {
            if (index == 0) {
                tree[0] += v;
                return;
            }
            while (index < tree.length) {
                tree[index] += v;
                index += index & (-index);
            }
        }

        public long read(int index) {
            index--;
            if (index == -1) {
                return 0;
            }
            long s = tree[0];
            while (index > 0) {
                s += tree[index];
                index -= index & (-index);
            }
            return s;
        }
    }

    public static void main(String [] args) throws IOException {
        InputReader ir = new InputReader(System.in);
        OutputWriter ow = new OutputWriter(System.out);
        int n = ir.readInt();
        int q = ir.readInt();
        Tree tree = new Tree(n);
        for (int i = 0; i < q; i++) {
            String command = ir.readString();
            if (command.equals("?")) {
                ow.printLine(tree.read(ir.readInt()));
            } else {
                tree.update(ir.readInt(), ir.readInt());
            }
        }
        ow.close();
    }


    public static class InputReader {

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
                if (c < '0' || c > '9') {
                    System.out.println("'" + c + "'");
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public boolean isSpaceChar(int c) {
            return isWhitespace(c);
        }

        public static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public char readCharacter() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            return (char) c;
        }
    }

    public static class OutputWriter {
            private final PrintWriter writer;

            public OutputWriter(OutputStream outputStream) {
                writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(
                        outputStream)));
            }

            public void close() {
                writer.close();
            }

            public void printLine(long i) {
                writer.println(i);
            }

            public void printLine(int i) {
                writer.println(i);
            }
        }
}
