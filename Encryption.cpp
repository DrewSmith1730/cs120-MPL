#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {
	// open file and pull all data into the vector
	vector<string> filetext;
	string temp;
	string fn = argv[2];
	string val = argv[1];
	int num = stoi(val);
	string choice = argv[3];
	ifstream fin;
	fin.open(fn);
	while (fin && fin.peek() != EOF) {
        getline(fin, temp, ' ');
        filetext.push_back(temp);
    }
    fin.close();
	
	// if encrypt is selected encrypt
	if(choice == "e"){
		for(int k = 0; k < num; k++) {
			for (int i = 0; i < filetext.size(); i++) {
				for (char &c : filetext[i]) {
					if(c != ' '){
						c += 2;
					}
				}
			}
		}
	}
	// if decrypt is selected decrypt
	if(choice == "d"){
		for(int k = 0; k < num; k++) {
			for (int i = 0; i < filetext.size(); i++) {
				for (char &c : filetext[i]) {
					if(c != ' '){
						c -= 2;
					}
				}
			}
		}
	}	
	
	ofstream fout;
    fout.open(fn);
    for(int i = 0; i < filetext.size(); i++){
        fout << filetext[i] << ' ';
    }
    fout.close();	
	

	return 0;
}