import java.util.*;

class Solution {
    class Node implements Comparable<Node> {
        int x, y, index;

        public Node(int x, int y, int index) {
            this.x = x;
            this.y = y;
            this.index = index;
        }

        @Override
        public int compareTo(Node other) {
            if (this.y == other.y) {
                return this.x - other.x;
            }
            return other.y - this.y;
        }
    }

    List<Integer> preOrderList = new ArrayList<>();
    List<Integer> postOrderList = new ArrayList<>();

    public int[][] solution(int[][] nodeinfo) {
        List<Node> nodes = new ArrayList<>();
        for (int i = 0; i < nodeinfo.length; i++) {
            nodes.add(new Node(nodeinfo[i][0], nodeinfo[i][1], i + 1));
        }

        Collections.sort(nodes);

        order(nodes);

        int[][] answer = new int[2][];
        answer[0] = preOrderList.stream().mapToInt(i -> i).toArray();
        answer[1] = postOrderList.stream().mapToInt(i -> i).toArray();

        return answer;
    }

    private void order(List<Node> graph) {
        if (graph.isEmpty()) {
            return;
        }

        Node root = graph.get(0);
        preOrderList.add(root.index);

        List<Node> leftSubtree = new ArrayList<>();
        List<Node> rightSubtree = new ArrayList<>();

        for (Node node : graph) {
            if (node.x < root.x) {
                leftSubtree.add(node);
            } else if (node.x > root.x) {
                rightSubtree.add(node);
            }
        }

        order(leftSubtree);
        order(rightSubtree);
        postOrderList.add(root.index);
    }
}
