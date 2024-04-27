package techne.com.br.ergonbi;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class ExecutePy {

    public void Processador (String arquivoPython, String diretorioArquivo) throws Exception {
        try {
        	
            // Comando para executar o script Python
            ProcessBuilder pb = new ProcessBuilder("python", arquivoPython);
        	
            // Definindo o diretório de trabalho
            pb.directory(new File(diretorioArquivo));
            
            // Redirecionando o output e o error stream
            pb.redirectErrorStream(true);
            
            // Iniciando o processo
            Process processo = pb.start();

            // Lendo a saída do processo
            BufferedReader reader = new BufferedReader(new InputStreamReader(processo.getInputStream()));
            String linha;
            while ((linha = reader.readLine()) != null) {
                System.out.println(linha);
            }

            // Esperando o processo finalizar
            int status = processo.waitFor();
            System.out.println("Término do processamento do aqruivo " + arquivoPython);

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
	
}
