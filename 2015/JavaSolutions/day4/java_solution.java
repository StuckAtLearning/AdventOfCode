import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Day4 {
    public static void main(String[] args) {
        int part1Answer = findSecretKeyMD5("iwrupvqb", 5);
        System.out.println(part1Answer);

        int part2Answer = findSecretKeyMD5("iwrupvqb", 6);
        System.out.println(part2Answer);
    }

    public static String covertStringToMD5(String inputPrefix) {
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(inputPrefix.getBytes());
            BigInteger no = new BigInteger(1, messageDigest);

            StringBuilder hashText = new StringBuilder(no.toString(16));
            while (hashText.length() < 32) {
                hashText.insert(0, "0");
            }
            return hashText.toString();
        }
        catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }

    public static int findSecretKeyMD5(String inputPrefix, int leadingZeroNum) {
        for (int i = 0; i <= 10000000; i++) {
            String md5Input = inputPrefix + i;
            String md5Output = covertStringToMD5(md5Input);
            if (md5Output.startsWith("0".repeat(leadingZeroNum))) {
                return i;
            }
        }
        return 0;
    }
}
