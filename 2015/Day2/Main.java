import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class Main {
    static ArrayList<String> input = new ArrayList<>();

    static void part1() {
        // List<String> input = List.of("1x1x10");
        int[] wrappingTotal = new int[] { 0 };

        input.forEach(surfaceStr -> {
            String[] dimensions = surfaceStr.split("x");
            int l = Integer.parseInt(dimensions[0]);
            int w = Integer.parseInt(dimensions[1]);
            int h = Integer.parseInt(dimensions[2]);
            int[] sides = new int[] { l * w, w * h, h * l };
            int smallest = Math.min(sides[0], Math.min(sides[1], sides[2]));

            wrappingTotal[0] += (2 * sides[0]) + (2 * sides[1]) + (2 * sides[2]) + smallest;
        });

        System.out.println(wrappingTotal[0]);
    }

    static void part2() {
        // List<String> input = List.of("1x1x10");

        int[] ribbonTotal = new int[] { 0 };

        input.forEach(surfaceStr -> {
            String[] dimensions = surfaceStr.split("x");
            int l = Integer.parseInt(dimensions[0]);
            int w = Integer.parseInt(dimensions[1]);
            int h = Integer.parseInt(dimensions[2]);
            int volume = l * w * h;
            int[] perimeters = new int[] { 2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h };
            int smallestPerimeter = Math.min(perimeters[0], Math.min(perimeters[1], perimeters[2]));

            ribbonTotal[0] += smallestPerimeter + volume;
        });

        System.out.println(ribbonTotal[0]);
    }

    public static void main(String[] args) {
        URL inputFileUrl = Main.class.getResource("input.txt");

        try (Stream<String> lines = Files.lines(Paths.get(inputFileUrl.toURI()))) {
            lines.forEach(line -> input.add(line));
        } catch (Exception e) {
            System.err.println(e);
            return;
        }

        // part1();
        part2();
    }

}