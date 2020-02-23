#include <stdio.h>

int main() {
	int iAmCool = 0xdeadbeef;

	char buf[20];
	printf("What's your name? ");
	fflush(stdout);

	scanf("%s", buf);
	if (iAmCool == 0xcafebabe) {
		printf("I think you're cool, so here's the flag!\n");
		printf("OWEEK{w3lc0me_t0_th3_c1uB!}\n");
		fflush(stdout);
		return 0;
	} else {
		printf("Sorry %s, you're currently not cool enough.\n", buf);
		fflush(stdout);
	}
	return 0;
}
