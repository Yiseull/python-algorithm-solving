class Solution {
    public String solution(String m, String[] musicinfos) {
        String answerTitle = "(None)";
        int answerPlayTime = 0;
        
        m = changeLower(m);
        for (String musicinfo : musicinfos) {
            String[] parts = musicinfo.split(",");
            String sheet = changeLower(parts[3]);
            int playTime = calculatePlayTime(parts[0], parts[1]);
            
            int i = 0;
            for (int j = 0; j < playTime; j++) {
                if (m.charAt(i) == sheet.charAt(j % sheet.length())) {
                    i++;
                    if (i == m.length()) {
                        if (answerPlayTime < playTime) {
                            answerTitle = parts[2];
                            answerPlayTime = playTime;
                        }
                        break;
                    }
                } else if (m.charAt(0) == sheet.charAt(j % sheet.length())) {
                    i = 1;
                    if (i == m.length()) {
                        if (answerPlayTime < playTime) {
                            answerTitle = parts[2];
                            answerPlayTime = playTime;
                        }
                        break;
                    }
                } else {
                    i = 0;
                }
            }
        }
        return answerTitle;
    }
    
    private static String changeLower(String sheet) {
        return sheet.replace("C#", "c")
                    .replace("D#", "d")
                    .replace("F#", "f")
                    .replace("G#", "g")
                    .replace("A#", "a")
                    .replace("B#", "b");
    }
    
    private static int calculatePlayTime(String start, String end) {
        String[] startParts = start.split(":");
        String[] endParts = end.split(":");
        return (Integer.parseInt(endParts[0]) * 60 + Integer.parseInt(endParts[1])) - (Integer.parseInt(startParts[0]) * 60 + Integer.parseInt(startParts[1]));
    }
}