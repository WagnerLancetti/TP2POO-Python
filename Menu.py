package TrabalhoPratico;

import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

import javax.swing.*;

public class Menu extends JFrame implements ActionListener{
	private static final long serialVersionUID = 1L;
	boolean menu = true;
    
	
    public void MenuPrincipal(){
    	ButtonGroup grupo = new ButtonGroup();
    	JLabel titulo2 = new JLabel("Marque o que deseja fazer:",SwingConstants.CENTER);
    	JLabel titulo = new JLabel("Menu Principal",SwingConstants.CENTER);
        setTitle("Menu");
        setSize(500,300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setVisible(true);
        setLayout(new GridLayout(6,1));
        setResizable(false);

        titulo.setFont(new Font("Arial",Font.BOLD,30));
        add(titulo);
        add(titulo2);

        ArrayList<JRadioButton> botao = new ArrayList<JRadioButton>();
        
        int i = 0;
        
        botao.add(new JRadioButton("Sair do Programa",true));
        botao.get(i).setHorizontalAlignment(SwingConstants.CENTER);
        add(botao.get(i));
        grupo.add(botao.get(i));
        i++;
        
        botao.add(new JRadioButton("Entrar no Menu de Locacoes",false));
        botao.get(i).setHorizontalAlignment(SwingConstants.CENTER);
        add(botao.get(i));
        grupo.add(botao.get(i));
        i++;        
        
        botao.add(new JRadioButton("Entrar no Menu de Carros",false));
        botao.get(i).setHorizontalAlignment(SwingConstants.CENTER);
        add(botao.get(i));
        grupo.add(botao.get(i));
        i++;
        
        JButton conf = new JButton("Confirmar");
        conf.setPreferredSize(new Dimension(10,10));
        conf.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent e){
	            if(botao.get(0).isSelected()){    
	            	System.exit(0);
	            }    
	            else if(botao.get(1).isSelected()){    
	            	MenuLoca m = new MenuLoca();
	            	m.Menu();
	            }
	            else if(botao.get(2).isSelected()){
//	               MenuCarro m = new MenuCarro();
//	               m.Menu();
	            }
	        }
    	});
        add(conf);
    }    
    
    public static void main (String []args){
    	Menu m = new Menu();
    	m.MenuPrincipal();
    }
	@Override
	public void actionPerformed(ActionEvent e) {
		// To aqui feliz deixa eu queto
		
	}
}
