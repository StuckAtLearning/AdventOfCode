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

        int ribbonLength = getRibbonLength(fileInfoInt);
        System.out.println(ribbonLength);
    }

    public static int getSurfaceArea(List<List<Integer>> presentDimensions) {
        List<Integer> eachSA = new ArrayList<>();
        for (List<Integer> eachDimension: presentDimensions) {
            int length = eachDimension.get(0);
            int height = eachDimension.get(1);
            int width = eachDimension.get(2);
            int[] sidesDimension = {length*height, length*width, height*width};

            int sa = Arrays.stream(sidesDimension).sum() * 2;
            int fullSA = sa + Arrays.stream(sidesDimension).min().getAsInt();
            eachSA.add(fullSA);
        }
//        return eachSA.stream().mapToInt(Integer::valueOf).sum();
        return eachSA.stream().reduce(0, Integer::sum);
    }

    public static int getRibbonLength (List<List<Integer>> presentDimensions) {
        List<Integer> eachLength = new ArrayList<>();
        for (List<Integer> eachDimension: presentDimensions) {
            int length = eachDimension.get(0);
            int height = eachDimension.get(1);
            int width = eachDimension.get(2);
            int[] halfSidePerimeter = {length+height, length+width, height+width};

            int partialLength = Arrays.stream(halfSidePerimeter).min().getAsInt() * 2;
            int fullLength = partialLength + (length*height*width);
            eachLength.add(fullLength);
        }
        return eachLength.stream().reduce(0, Integer::sum);
    }
}
