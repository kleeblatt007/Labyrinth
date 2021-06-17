import java.util.LinkedList;
import java.util.List;
import java.util.Stack;
/**
 * Class that represents a maze with N*N junctions.
 * 
 * @author Vera Röhr
 */
public class Maze{
    private final int N;
    private Graph M;    //Maze
    public int startnode;
        
	public Maze(int N, int startnode) {
		
        if (N < 0) throw new IllegalArgumentException("Number of vertices in a row must be nonnegative");
        this.N = N;
        this.M= new Graph(N*N);
        this.startnode= startnode;
        buildMaze();
	}
	
    public Maze (In in) {
    	this.M = new Graph(in);
    	this.N= (int) Math.sqrt(M.V());
    	this.startnode=0;
    }

	
    /**
     * Adds the undirected edge v-w to the graph M.
     *
     * @param  v one vertex in the edge
     * @param  w the other vertex in the edge
     * @throws IllegalArgumentException unless both {@code 0 <= v < V} and {@code 0 <= w < V}
     */
    public void addEdge(int v, int w) {
		// TODO
        M.addEdge(v,w);
    }
    
    /**
     * Returns true if there is an edge between 'v' and 'w'
     * @param v one vertex
     * @param w another vertex
     * @return true or false
     */
    public boolean hasEdge( int v, int w){
		// TODO
        if (v == w){
            return true;
        }
        if (v < 0 || v > M.V() || w < 0 || w > M.V()){
            return false;
        }
        for (int x : M().adj(v)){
            if (x == w){
                return true;
            }
        }
        return false;
    }	
    
    /**
     * Builds a grid as a graph.
     * @return Graph G -- Basic grid on which the Maze is built
     */
    public Graph mazegrid() {
		// TODO
        Graph G = new Graph(M.V());
        if (M.V() < 2){
            return G;
        }
        int v = 0;
        for (int y = 0; y < N; y++){
            for (int x = 0; x < N; x++){
                if (y == 0){
                    if (x == 0){
                        if (!G.adj(v).contains(v+1)){
                            G.addEdge(v,v+1);
                        }
                        if (!G.adj(v).contains(v+N)){
                            G.addEdge(v,v+N);
                        }

                    }else if (x == N-1){
                        if (!G.adj(v).contains(v-1)){
                            G.addEdge(v,v-1);
                        }
                        if (!G.adj(v).contains(v+N)){
                            G.addEdge(v,v+N);
                        }
                    }else {
                        if (!G.adj(v).contains(v+1)){
                            G.addEdge(v,v+1);
                        }
                        if (!G.adj(v).contains(v-1)){
                            G.addEdge(v,v-1);
                        }
                        if (!G.adj(v).contains(v+N)){
                            G.addEdge(v,v+N);
                        }
                    }
                }else if (y == N-1){
                    if (x == 0){
                        if (!G.adj(v).contains(v-N)){
                            G.addEdge(v,v-N);
                        }
                        if (!G.adj(v).contains(v+1)){
                            G.addEdge(v,v+1);
                        }
                    }else if (x == N-1){
                        if (!G.adj(v).contains(v-N)){
                            G.addEdge(v,v-N);
                        }
                        if (!G.adj(v).contains(v-1)){
                            G.addEdge(v,v-1);
                        }
                    }else {
                        if (!G.adj(v).contains(v-N)){
                            G.addEdge(v,v-N);
                        }
                        if (!G.adj(v).contains(v-1)){
                            G.addEdge(v,v-1);
                        }
                        if (!G.adj(v).contains(v+1)){
                            G.addEdge(v,v+1);
                        }
                    }
                }else {
                    if (x == 0){
                        if (!G.adj(v).contains(v-N)){
                            G.addEdge(v,v-N);
                        }
                        if (!G.adj(v).contains(v+N)){
                            G.addEdge(v,v+N);
                        }
                        if (!G.adj(v).contains(v+1)){
                            G.addEdge(v,v+1);
                        }
                    }else if (x == N-1){
                        if (!G.adj(v).contains(v-N)){
                            G.addEdge(v,v-N);
                        }
                        if (!G.adj(v).contains(v+N)){
                            G.addEdge(v,v+N);
                        }
                        if (!G.adj(v).contains(v-1)){
                            G.addEdge(v,v-1);
                        }
                    }else {
                        if (!G.adj(v).contains(v-N)){
                            G.addEdge(v,v-N);
                        }
                        if (!G.adj(v).contains(v+N)){
                            G.addEdge(v,v+N);
                        }
                        if (!G.adj(v).contains(v-1)){
                            G.addEdge(v,v-1);
                        }
                        if (!G.adj(v).contains(v+1)){
                            G.addEdge(v,v+1);
                        }
                    }
                }
                v++;
            }
        }
        return G;
    }

    private void validateVertex(int v) {
        int V = M.V();
        if (v < 0 || v >= V)
            throw new IllegalArgumentException("vertex " + v + " is not between 0 and " + (V));
    }
    
    /**
     * Builds a random maze as a graph.
     * The maze is build with a randomized DFS as the Graph M.
     */
    private void buildMaze() {
		// TODO
        RandomDepthFirstPaths G = new RandomDepthFirstPaths(M,startnode);
        if (M.V() < 2){
            return;
        }
        G.randomDFS(mazegrid());
        int[] a = G.edge();
        for (int i = 0; i < a.length; i++){
            if(i == startnode){
                continue;
            }
            addEdge(i,a[i]);
        }
    }

    /**
     * Find a path from node v to w
     * @param v start node
     * @param w end node
     * @return List<Integer> -- a list of nodes on the path from v to w (both included) in the right order.
     */
    public List<Integer> findWay(int v, int w){
		// TODO
        validateVertex(v);
        validateVertex(w);
/*
        List<Integer> path = new LinkedList<>();
        if (v == w){
            path.add(v);
            return path;
        }
        while (v != w){
            path.add(v);
            v = M.adj(v).getFirst();
            if (v == 0){
                return null;
            }
        }
        return path;
        */
        DepthFirstPaths path = new DepthFirstPaths(M,w);
        path.dfs(M);

        return path.pathTo(v);
    }
    
    /**
     * @return Graph M
     */
    public Graph M() {
    	return M;
    }

    public static void main(String[] args) {
		// FOR TESTING
        Maze m = new Maze(5,0);
        m.mazegrid();

    }


}
