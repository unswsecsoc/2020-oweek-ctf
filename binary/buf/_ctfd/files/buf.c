#include <stdio.h>

int main() {
	int iAmCool = 0xdeadbeef;

	char buf[20];
	printf("What's your name? ");
	scanf("%s", buf);
	if (iAmCool == 0xcafebabe) {
		printf("I think you're cool, so here's the flag!\n");
		printf("OWEEK{<redacted>}\n");
		return 0;
	} else {
		printf("Sorry %s, you're currently not cool enough.\n", buf);
	}
	return 0;
}
