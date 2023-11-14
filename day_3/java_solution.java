import java.nio.file.Path;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Day3 {
    public static void main(String[] args) {
        String elfPathInfo = parseInputPathInfo("inputs/day_3_real_input.txt");
        InputManager.Coordinate beginnerLocation = new InputManager.Coordinate(0, 0);
        int part1Answer = getVisitedLocations(elfPathInfo, beginnerLocation).size();
        int part2Answer = getVisitedLocationsWithRobot(elfPathInfo, beginnerLocation);
        System.out.println(part1Answer);
        System.out.println(part2Answer);
    }

    public static String parseInputPathInfo(String inputFilePath) {
        return InputManager.readFile(Path.of(inputFilePath)).get(0);
    }

    public static Set<InputManager.Coordinate> getVisitedLocations(String pathInfo, InputManager.Coordinate startLocation) {
        List<InputManager.Coordinate> pathDirections = InputManager.parseDirections(pathInfo);
        Set<InputManager.Coordinate> seenLocation = new HashSet<>();
        seenLocation.add(startLocation);

        for (InputManager.Coordinate direction: pathDirections) {
            InputManager.Coordinate nextLocation = startLocation.moveCoordinate(direction);
            startLocation = nextLocation;
            seenLocation.add(nextLocation);
        }
        return seenLocation;
    }

    public static String getSubString(String pathInfo, int startIndex, int endIndex, int gapIndexNum) {
        StringBuilder subString = new StringBuilder();
        for (int i = startIndex; i < endIndex; i += gapIndexNum) {
            subString.append(pathInfo.charAt(i));
        }
        return subString.toString();
    }

    public static int getVisitedLocationsWithRobot(String pathInfo, InputManager.Coordinate startLocation) {
        String santaPath = getSubString(pathInfo, 0, pathInfo.length(), 2);
        String robotPath = getSubString(pathInfo, 1, pathInfo.length(), 2);

        Set<InputManager.Coordinate> santaLocations = getVisitedLocations(santaPath, startLocation);
        Set<InputManager.Coordinate> robotLocations = getVisitedLocations(robotPath, startLocation);
        Set<InputManager.Coordinate> unionLocations = new HashSet<>(santaLocations);
        unionLocations.addAll(robotLocations);

        return unionLocations.size();
    }

}
