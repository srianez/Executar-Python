package techne.com.br.ergonbi;

public class CallPython {
	
    public static void main(String[] args) {
        ExecutePy executePy = new ExecutePy();
		try {
			executePy.Processador("ExtractFuncionarios.py", "python_scripts");
		} catch (Exception e) {
			e.printStackTrace();
		}
    }
}
