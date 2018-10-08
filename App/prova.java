import java.util.Scanner; //Llibreria per llegir dades del teclat
public class prova {
	private static final double IVA = 0.18;
    public static void main(String[] args) {
        Scanner lector = new Scanner(System.in); //Inicialitzar la llibreria per a llegir text
    	int a = 21;
    	String text = "foo";
        System.out.println("Hola, mon!");
        System.out.println(true);
        System.out.println("L\'IVA actual es de: "+IVA);
        System.out.print((long)a);
        System.out.println(text);
        System.out.println("\\n: a\nb");
        System.out.println("\\t: a\tb");
        System.out.println("\\\': a\'b");
        System.out.println("\\\": a\"b");
        System.out.println("\\\\: a\\b");
        System.out.println("Enter larg: "+3000000000L);
        System.out.println("El codi ascii de g: "+(int)'g');
        System.out.print("Introduexi un enter: ");
        int intInput = lector.nextInt(); //Legeix Int, canviar Int per a Float, Long, Byte, etc (excepte String i Char) per a obtenir la dada esperada
        System.out.println("Has introduit: "+intInput);
        lector.nextLine(); //Desplaca a seguent linia
        System.out.print("Introduexi un text: ");
        String StrInput = lector.next();
        System.out.println("Has introduit: "+StrInput);
        lector.nextLine(); //Desplaca a seguent linia
        System.out.print("Introduexi un bolea (true o false): ");
        Boolean BoolInput = lector.nextBoolean();
        if(BoolInput) //Sense claudators nomes executa la primara, encara que la resta estiguin sagnades
            System.out.println("1+2=3");
        else{ //Amb claudators no hi ha maxim de comandes
            System.out.println("1+2=4");
        }
        lector.nextLine(); //Desplaca a seguent linia
        System.out.print("Introduexi un nombre: ");
        intInput = lector.nextInt(); //Legeix Int, canviar Int per a Float, Long, Byte, etc (excepte String i Char) per a obtenir la dada esperada
        if(intInput==0)
            System.out.println("El valor es: 0");
        else if(intInput>0)
            System.out.println("El valor es positiu");
        else
            System.out.println("El valor es negatiu");
        System.out.print("Amb els nombres 4 i 2 es poden fer diferents operacions: 1 per a sumar, 2 per a restar, 3 per a multiplicar i 4 per a dividir: ");
        lector.nextLine();
        switch(lector.nextInt()){
            case 1: //":"" en plan python
                System.out.println("Ha escollit sumar 4+2, que dona 6");
                break; //En lloc d'indentacio s'atura al trubar un altre case, o si troba un break que surt fora del swich
            case 0:
                System.out.println("0.");
                //Com que no te break executa el default
            case 2:
                System.out.println("Ha escollit restar 4-2, que dona 2");
                break;
            case 3:
                System.out.println("Ha escollit multiplicar 4*2, que dona 8");
                break;
            case 4:
                System.out.println("Ha escollit dividir 4/2, que dona 2");
                break;
            default: //Per als valors que no estan al case o drespres d'executar-los (si no han sortit del swich(break))
                System.out.println("Ho sentim, pero hi ha agut un error: l\'operacio no es valida");
        }
        System.out.println("Comptadors:\nWhile:");
        int i = 0;
        while(i<10)
            System.out.println(i++);
        System.out.println("Do While");
        int k =0;
        do//El Do While primer executa i despres mira la condicio, al inreves que el while normal
            System.out.println(k++);
        while(k<10);//En aquest exemple no es nota la diferencia
        System.out.println("For:");
        for(int j=0;j<10;j++)
            System.out.println(j);
        System.out.println("Arrays:");
        int[] Arr = new int[10]; //Definim l'array Arr, que es d'enters i de mida 10
        int[] array = {0,0,0,0,0,0,0,0,0,0}; //Fem el mateix, pero individualment
        System.out.println(array.length); //Conseguin la llargada de l'array array
        for(int j=0;j<Arr.length;j++) //El for, per exemple, tambe serveix per a iterar enyre els elements de l'array Arr
            System.out.println(Arr[j]);
        System.out.print("Ara canviarem uns valors de l\'altre array\nSeleccioni posicio (1-10)");
        lector.nextLine();
        int index = lector.nextInt();
        System.out.print("Ha escollit la posicio "+index+", que correspon al valor "+array[index-1]+"\nSeleccioni el nou enter per a aquesta posicio: "); //Imprimim per pantalla les instruccions, com que les posicins comencant amb el 0, restem 1 al index
        lector.nextLine();
        array[index-1] = lector.nextInt(); //Redefinim el valor de l'array
        float[] llistaNotes = {5.5f, 9f, 2f, 10f, 4.9f};
        //El mostrem per pantalla.
        System.out.print("L\'array sense ordenar es: [ ");
        for (int o = 0; o < llistaNotes.length; o++) {
            System.out.print(llistaNotes[o] + " ");
        }
        System.out.println("]");
        //Bucle extern.
        //S’anirà posant a cada posició tractada, començant per la 0,
        //el valor més baix que es trobi.
        for (int p = 0; p < llistaNotes.length - 1; p++) {
            //Bucle intern.
            //Se cerca entre la resta de posicions quin és el valor més baix.
            for(int j = p + 1; j < llistaNotes.length; j++) {
                //La posició tractada té un valor més alt que el de la cerca. Els intercanviem.
                if (llistaNotes[p] > llistaNotes[j]) {
                    //Per intercanviar valors cal una variable auxiliar.
                    float canvi = llistaNotes[p];
                    llistaNotes[p] = llistaNotes[j];
                    llistaNotes[j] = canvi;
                }
            }
        }
        //El mostrem per pantalla.
        System.out.print("L\'array ordenat es: [ ");
        for (int o = 0; o < llistaNotes.length; o++) {
            System.out.print(llistaNotes[o] + " ");
        }
        System.out.println("]");
        int[][] arraybidi = new int[5][5];
        int[][] arrbidi = {{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}};
        for(int j=0;j<arrbidi.length;j++){
            for(int h=0;h<arrbidi[j].length;h++){
                System.out.println("Pos: ["+j+"]["+h+"]\nArraybidimensional1: "+arrbidi[j][h]+"\nArraybidimensional2: "+arraybidi[j][h]+"\n==================================");
            }
        }
    }
}