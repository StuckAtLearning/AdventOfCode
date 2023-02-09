import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
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
}
