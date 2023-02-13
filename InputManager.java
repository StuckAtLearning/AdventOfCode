import java.io.IOException;
import java.nio.MappedByteBuffer;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.MatchResult;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class InputManager {
    public static List<String> readFile(Path filePath) {
        try {
            return Files.readAllLines(filePath);

        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }


    public static List<List<String>> groupFileWithDoubleNewLine(List<String> fileInfo) {
        List<List<String>> groupedInfo = new ArrayList<>();
        List<String> group = new ArrayList<>();
        for (String info : fileInfo) {
            if (info.isEmpty()) {
                groupedInfo.add(group);
                group = new ArrayList<>();
            } else {
                group.add(info);
            }
        }
        groupedInfo.add(group);
        return groupedInfo;
    }


    public static List<Integer> parseIntInLine(String info, boolean includeNegatives) {
        Pattern intPattern;
        if (includeNegatives) {
            intPattern = Pattern.compile("-?\\d+");
        }
        else {
            intPattern = Pattern.compile("\\d+");
        }
        Matcher inputInfo = intPattern.matcher(info);
        List<String> parsedInfo = inputInfo.results().map(MatchResult::group).toList();
        return parsedInfo.stream().map(Integer::valueOf).toList();
    }

//    record Point(int x, int y)
//    {
//        Point add(Point other) {
//            return new Point(this.x + other.x, this.y + other.y);
//        }
//
//        Point rotate() {
//            return new Point(this.y, -this.x);
//        }
//
//        Point offset(Direction d) {}
//    }

//    enum Direction {
//        NORTH, EAST, WEST, SOUTH;
//
//        int x() {}
//        int y() {}
//    }
//
//    List<Direction> foo1() {
//        return List.of(Direction.EAST);
//    }

    record Coordinate(int x, int y) {
        Coordinate moveCoordinate(Coordinate step) {
            return new Coordinate(this.x + step.x, this.y + step.y);
        }
    }

    public static List<Coordinate> parseDirections(String lineInfo) {
        Map<Character, Coordinate> directionLookUp = new HashMap<>();

        Coordinate goRightMovement = new Coordinate(1, 0);
        Coordinate goLeftMovement = new Coordinate(-1, 0);
        Coordinate goUpMovement = new Coordinate(0, 1);
        Coordinate goDownMovement = new Coordinate(0, -1);

        directionLookUp.put('>', goRightMovement);
        directionLookUp.put('<', goLeftMovement);
        directionLookUp.put('^', goUpMovement);
        directionLookUp.put('v', goDownMovement);

        List<Coordinate> parsedDirections = new ArrayList<>();
        for (char c: lineInfo.toCharArray()) {
            parsedDirections.add(directionLookUp.get(c));
        }
        return parsedDirections;
    }
}
