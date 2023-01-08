#include <cmath>
#include <bits/stdc++.h>
using namespace std;

struct input
{
    char data; // code word
    float pro;// probability of code word
} typedef input;

struct output
{
    char data;// code word
    int len; // length of code word
    int *bin; // binary
} typedef output;

struct result
{
    char* data;
    int** bin;
} typedef result;

//sort codewords in descending order of probability
void sortByProbability(int size, struct input p[])
{
	int i, j;
	struct input temp;
	for (j = 1; j <= size - 1; j++) {
		for (i = 0; i < size - 1; i++) {
			if ((p[i].pro) < (p[i + 1].pro)) {
				temp.pro = p[i].pro;
				temp.data = p[i].data;

				p[i].pro = p[i + 1].pro;
				p[i].data = p[i + 1].data;

				p[i + 1].pro = temp.pro;
				p[i + 1].data = temp.data;
			}
		}
	}
}

struct input* sumPro(int size, struct input p[])
{
    int i,j;
    struct input* cInput = nullptr;
    cInput = (struct input*)malloc(size*sizeof(struct input));

    for( i = 0; i< size; i++)
    {
        cInput[i].data = p[i].data;
        cInput[i].pro = 0;
        for(j = i-1; j>= 0;j--)
        {
            cInput[i].pro +=p[j].pro;
        } 
    }

    return cInput;
};

void lenCal(int size,struct input pI[], struct output pO[])
{
    for(int i = 0; i < size; i++)
    {
        pO[i].len = (-(log2(pI[i].pro))) + 1;
    };
};

//cal binary form of probability
void binCal(int size, struct input pI[], struct output pO[])
{
    float temp;
     
    for(int  i = 0; i< size; i++)
    {
        temp = pI[i].pro; 
        pO[i].bin = (int*)malloc((pO[i].len)*sizeof(int));
        for(int j = 0; j < pO[i].len ; j++)
        {
            pO[i].bin[j] = (int)(temp*2);
            temp = temp*2 - (int)(temp*2);
        }
    }
};

//function to cal avgLen of output
float avgLen(int size ,struct input pI[], struct output pO[]){
	float avglen = 0;
	for(int i = 0; i < size; i++){
		avglen += (pO[i].len + 1)* pI[i].pro;
	}
	return avglen;
} 

//function to cal entropy 
float entropy(int size ,struct input pI[]){
	float entropy = 0;
	for(int i = 0; i < size; i++){
		entropy -= pI[i].pro* log2(pI[i].pro);
	}
	return entropy;
} 

void display(int size, struct input pIR[],struct input pIC[], struct output pO[])
{
	int i, j;
	cout << "\n\n\n\tSymbol\tpi\tPj\tCode";
	for (i = 0; i <size; i++) {
		cout << "\n\t" << pIR[i].data << "\t" << pIR[i].pro << "\t" << pIC[i].pro << "\t";
		for (j = 0; j < pO[i].len; j++)
			cout << pO[i].bin[j];
	}
	cout << "\navglen : " << avgLen(size,pIR,pO) << endl;
	cout << "entropy: " << entropy(size,pIR) << endl; 
}

struct result shanonCoding(char data[], float pro[], int size)
{
    struct input* rInput;// array raw input
    rInput = (struct input*)malloc(size*sizeof(struct input));

    struct input* cInput;// array changed(sum of probability) input
    cInput = (struct input*)malloc(size*sizeof(struct input));

    struct output* output;// array of output
    output = (struct output*)malloc(size*sizeof(struct output));

    int i,j;

    //enter value for input
    for(i = 0; i<size; i++)
    {
        rInput[i].data = data[i];
        rInput[i].pro = pro[i];
    };

    // sort raw input
    sortByProbability(size,rInput);
    for(i = 0; i<size; i++)
    {
        output[i].data = rInput[i].data;
    };

    //calculator probability of changed input 
    cInput = sumPro(size,rInput);

    //calculator length of changed input
    lenCal(size,rInput,output);

    //calculator binary form of changed input
    binCal(size,cInput,output);

    display(size,rInput,cInput,output);

    //return
    struct result result;
    result.data = (char*)malloc(sizeof(char) * size);
    result.bin = (int**)malloc(sizeof(int*) * size);
    for( int i = 0; i < size; i++)
    {
        result.data[i] = cInput[i].data;
        result.bin[i]  = output[i].bin;
    } ;

    return result;
}


int main()
{
    cout <<"SHANNON CODING" << endl;
    int n = 10;
	char y[] = {'a','b','c','d','e','f','g','h','i','k'};
	float x[] = { 0.13,0.07,0.02, 0.18,0.06,0.04, 0.15, 0.160, 0.05, 0.14 };
	shanonCoding(y,x,n);
    return 0;
}