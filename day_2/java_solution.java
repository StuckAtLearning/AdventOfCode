import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Day2 {
    public static void main(String[] args) {
        List<String> fileInfo = InputManager.readFile(Path.of("inputs/day_2_real_input.txt"));
        List<List<Integer>> fileInfoInt = fileInfo.stream()
                .map(x -> InputManager.parseIntInLine(x, false).stream().toList()).toList();
        System.out.println(fileInfoInt);

        int wrappingPaperSA = getSurfaceArea(fileInfoInt);
        System.out.println(wrappingPaperSA);
    }

    public static int getSurfaceArea(List<List<Integer>> presentDimensions) {
        List<Integer> eachSA = new ArrayList<>();
        for (List<Integer> eachDimension: presentDimensions) {
            int length = eachDimension.get(0);
            int height = eachDimension.get(1);
            int width = eachDimension.get(2);
            int[] dimension = {length, height, width};

            int sa = 2 * (length*height + length*width + height*width);
            int fullSA = sa + Arrays.stream(dimension).min().getAsInt();
            eachSA.add(fullSA);
        }
//        return eachSA.stream().mapToInt(Integer::valueOf).sum();
        return eachSA.stream().reduce(0, Integer::sum);
    }
}
