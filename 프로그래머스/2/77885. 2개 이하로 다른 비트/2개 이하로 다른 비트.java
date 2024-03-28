class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];
        
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] % 2 == 0) {
                answer[i] = numbers[i] + 1;
            } else {
                StringBuilder sb = new StringBuilder(Long.toBinaryString(numbers[i]));
                int zero = sb.lastIndexOf("0");
                if (zero == -1) {
                    sb.setCharAt(0, '0');
                    sb.insert(0, "1");
                } else {
                    sb.setCharAt(zero, '1');
                    sb.setCharAt(zero + 1, '0');
                }
                answer[i] = Long.parseLong(sb.toString(), 2);
            }
        }
        
        return answer;
    }
}