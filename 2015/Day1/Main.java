import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.stream.Stream;

/**
 * main
 */
public class Main {

    static void part1(int start, char[] input) {
        int currentFloor = start;

        for (char i : input) {
            if (i == '(') {
                currentFloor++;
            } else if (i == ')') {
                currentFloor--;
            }
        }

        System.out.println(currentFloor);
    }

    static void part2(int startingFloor, String input) {
        int currentFloor = startingFloor;

        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == '(') {
                currentFloor++;
            } else if (input.charAt(i) == ')') {
                currentFloor--;
            }

            if (currentFloor < 0) {
                System.out.println(i + 1);
                return;
            }
        }
    }

    public static void main(String[] args) {
        URL inputFileUrl = Main.class.getResource("input.txt");
        ArrayList<String> input = new ArrayList<>();

        try (Stream<String> lines = Files.lines(Paths.get(inputFileUrl.toURI()))) {
            lines.forEach(line -> input.add(line));
        } catch (Exception e) {
            System.err.println(e);
            return;
        }

        int startingFloor = 0;
        String tempInput = "()())";
        // part1(startingFloor, input.get(0).toCharArray());
        // part2(startingFloor, tempInput);
        part2(startingFloor, input.get(0));
    }
}