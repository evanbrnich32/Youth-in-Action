// Program to develop an inspiring platform for 'Youth in Action' 
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int age;
    char name[30];
    char goals[100];

    // Get basic information from user
    printf("Enter your name: ");
    gets(name);
    printf("Enter your age: ");
    scanf("%d", &age);

    // Give user an introduction to `Youth in Action`
    printf("Hey %s, welcome to Youth in Action!\n", name);
    printf("We are an inspiring platform for young people who want to make a difference.\n");
    printf("Tell us about your goals, and we will help you reach them!\n");

    // Get user's goals
    printf("Goals: ");
    gets(goals);

    // Offer user resources and feedback
    printf("We are here to help you reach your goals! Here are some resources and feedback you might find useful.\n");
    printf("If you're %d years old, you should consider...\n", age);

    // Age-based resources & feedback
    if(age < 18)
    {
        printf("- Researching local volunteer opportunities\n");
        printf("- Surrounding yourself with people who support your goals\n");
        printf("- Developing a skill and mastering it\n");
    }
    else if(age >= 18 && age < 25)
    {
        printf("- Joining a club or organization related to your goals\n");
        printf("- Networking with professionals in your field\n");
        printf("- Developing a plan for accomplishing your goals\n");
    }
    else
    {
        printf("- Applying for a leadership position in your field\n");
        printf("- Researching grant opportunities\n");
        printf("- Mentoring younger generations\n");
    }

    // General resources & feedback
    printf("- Researching people who have achieved similar goals\n");
    printf("- Setting reasonable, achievable goals\n");
    printf("- Taking your time and celebrating milestones\n\n");

    // Conclude
    printf("Remember, Youth in Action is here for you! You can do this.\n");

    return 0;
}