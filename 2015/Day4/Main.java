import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HexFormat;

public class Main {
    static String input = "iwrupvqb";

    static String getMd5(String secret) {
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] hashBytes = md.digest(secret.getBytes(StandardCharsets.UTF_8));

            return HexFormat.of().formatHex(hashBytes);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("MD5 algorithm not found", e);
        }
    }

    static void findLowestPositiveNumber(String secretKey, String prefix) {
        int secretNumber = -1;
        String hash = "";

        while (!hash.startsWith(prefix)) {
            hash = getMd5(secretKey + ++secretNumber);
        }
        System.out.println(hash);
        System.out.println(secretNumber);
    }

    public static void main(String[] args) {
        // String input = "pqrstuv";
        String prefix = "000000";
        findLowestPositiveNumber(input, prefix);
    }
}