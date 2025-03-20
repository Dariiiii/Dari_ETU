#include <stdio.h>
#include <stdlib.h>

#define LINE_SIZE 128

int main(int argc, char* argv[])
{
	if (argc != 2)
	{
		return 0;
	}
	FILE* file = NULL;
	file = fopen(argv[1], "r");
	if (!file)
	{
		printf("%s: file %s unreacheble\n", argv[0], argv[1]);
		return -1;
	}
	char line[LINE_SIZE];
	while (fgets(line, sizeof(line), file))
	{
		printf("%s", line);
	}
	fclose(file);
	
	return 0;
}
