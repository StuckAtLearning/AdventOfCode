import java.nio.file.Path;
import java.util.List;

public class Day1 {
    public static void main(String[] args) {
        Path inputFilePath = Path.of("inputs/day_1_real_input.txt");
        List<String> inputs = InputManager.readFile(inputFilePath);
        int floorNum = getFloorNum(inputs);
        System.out.println(floorNum);
        int inputPosition = getInputPosition(inputs);
        System.out.println(inputPosition);
    }

    public static int getFloorNum(List<String> inputLines) {
        String inputLine = inputLines.get(0);
        int floorNum = 0;
        for (char eachChar : inputLine.toCharArray()) {
            if (eachChar == '(') {
                floorNum++;
            } else {
                floorNum--;
            }
        }
        return floorNum;
    }

    public static int getInputPosition(List<String> inputLines) {
        String inputLine = inputLines.get(0);
        int floorNum = 0;
        int inputPosition = 1;
        for (char eachChar : inputLine.toCharArray()) {
            if (floorNum == -1) {
                return inputPosition;
            }
            if (eachChar == '(') {
                floorNum++;
            } else {
                floorNum--;
            }
            inputPosition ++;
        }
        return floorNum;
    }
}