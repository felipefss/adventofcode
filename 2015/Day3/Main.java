import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.stream.Stream;

record Point(int x, int y) {
}

public class Main {
    static ArrayList<String> input = new ArrayList<>();

    static Point nextHouse(char move, int x, int y) {
        switch (move) {
            case '^':
                return new Point(x, y + 1);
            case 'v':
                return new Point(x, y - 1);
            case '>':
                return new Point(x + 1, y);
            case '<':
                return new Point(x - 1, y);
        }

        return null;
    }

    static void part1(char[] moves) {
        var visitedHouses = new HashSet<Point>();
        visitedHouses.add(new Point(0, 0));
        int x = 0;
        int y = 0;

        for (char move : moves) {
            var current = nextHouse(move, x, y);
            x = current.x();
            y = current.y();
            visitedHouses.add(current);
        }

        System.out.println(visitedHouses.size());
    }

    static void part2(char[] moves) {
        var visitedHouses = new HashSet<Point>();
        visitedHouses.add(new Point(0, 0));
        int santaX = 0;
        int santaY = 0;
        int robotX = 0;
        int robotY = 0;

        for (int i = 0; i < moves.length - 1; i += 2) {
            char santaMove = moves[i];
            var current = nextHouse(santaMove, santaX, santaY);
            santaX = current.x();
            santaY = current.y();
            visitedHouses.add(current);

            char robotMove = moves[i + 1];
            current = nextHouse(robotMove, robotX, robotY);
            robotX = current.x();
            robotY = current.y();
            visitedHouses.add(current);
        }

        System.out.println(visitedHouses.size());
    }

    public static void main(String[] args) {
        URL inputFileUrl = Main.class.getResource("input.txt");

        try (Stream<String> lines = Files.lines(Paths.get(inputFileUrl.toURI()))) {
            lines.forEach(line -> input.add(line));
        } catch (Exception e) {
            System.err.println(e);
            return;
        }

        // List<String> input = List.of("^v^v^v^v^v");

        // part1(input.get(0).toCharArray());
        part2(input.get(0).toCharArray());
    }
}