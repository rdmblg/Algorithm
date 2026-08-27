#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <stdbool.h>

//int sum(int x, int y) {
//    return x + y;
//}
//
int main() {
    printf("�ȳ�");
//{
//    int val = sum(1, 2);
//    printf("%d", val);
    //�����
    //printf("Hello World!\n");
    //printf("Hello \n");

    // ������, �Ǽ���, ������
    // ������: int, long long, unsighed int, unsigned long long
    // int 4byte�ڷ���, long long 8byte�ڷ���
    // 00000000
    // 1 byte = 8bit
    // int: -�� -20�� ~ 20�� -2^31 ~ 2^31 -1
    // long long ; -2^63 ~ 2^63 -1

    // �Ǽ���
    // float : 32bit = 4byte, double = 8byte;

    // ������
    // char a = 'a'; // 1byte
    // -128 ~ 127
    //char a = 'a';
    //printf("%d\n", a);
    //printf("%d\n", a - 'a');
    //char b = '9';
    //printf("%d\n",  b - '0');
    // boolean c��� �⺻������ ����
    // bool isfalse = true ;

    // printf
    //printf("asdf %d \n", 10);  //#d�� �����ʿ��� ������ ã�Ƽ� �ִ°� 
    //printf("asdf %f \n", 3.314f);  //#f�� ���������� �Ǽ��� ã�Ƽ� �ִ°�
    //int z = 1;
    //printf("%c, %d, %d\n", 'z', z, 12);

    //int x;
    //int y = 1;
    //printf("%d", &y);
    //&y;
    //scanf("%d", &x);
    //scanf_s("%d", &y);

    // �Ǽ� 10�� �Է¹޾� ���:
    // float a;
    // scanf("%f", &a);
    // printf("print: %f\n", a);

    // ++, --

    //int i = 1;
    //++i; // i = i + 1;
    //i++;
    //val = i++;  val = 1; i = 2;
    //val = ++i; // i = 2 ; val = 2;

    // printf("%d", ++i);
    //�Ҵ� ������
    // +=, -=, *=, /=, %=
    // i = i + 1;
    // i += 1;
    // i -= 1;
    // i *= 2;
    // i /= 2;
    // i %= 2;
    //��Ʈ������
    // 1 ����Ʈ = 8 ��Ʈ
    //00000000
    // 1111 & 0001 = �� �� 1�ΰ�쿣1 �ƴϸ� 0 == 0001
    // 1111 | 0000 = �� ��Ʈ �� �ϳ��� 1 �̸� 1 == 1111
    // 1111 ^ 1100 = �� ��Ʈ�� ���� �ٸ� �� 1�� ��ȯ == 0011
    // ~0000 = 1111 
    // val = 2 << 3; 00000010 00100000  a << b; a x 2 ^ b
    // val = 2 >> 3; // a >> b  a / 2^b

    //���׿�����
    // int data = 10;
    // data == 20 ? data = 100 : data = 200;
    // (����) ? ���϶� ���: ������ �� ���

    // boolean true / false �� ����
    // bool isfalse = true;  // 0 = false, 0�� ������ ������ true
    // isfalse = 0;
    // isfalse = 10;

    //bool isfalse = true;

    // ���迬����
    // <, >, <=, >=, == !=
    //(1 < 10);
    // ����������
    // && and, || or, ! not
    // if () {
    //     //
    // }
    // else {
    //     printf();
    //     //
    // }

    //������ ����
    // 1. ��������
    // int a = 10;
    // for (){
    //     int b = 10;
    // }
    // b = 10;
    // if (){

    // }  //�Լ� �ȿ��� ���ǵ� �ֵ��� �Լ� �ۿ��� �� �� ����

    // 2. ��������
    // �����ϸ� �����Լ� �ٱ����� ����
    // int c = 1;

    // int add(){
    //     int a = 10;
    //     c = 10;
    // }

    //int main() {}

    // 3. ��������
    // 4. �ܺκ���

    // �Է� : r;
    // ��� : ����; pi * r ^ 2
    // float r;
    // scanf("%f", &r);
    // const float PI = 3.141592f;
    // printf("%f", PI * r * r);

    //���ǹ�
    // if ��
    // if(����) {
    //�ڵ�}

    // int age = 20;

    // if (age >= 20) {
    //     printf("�ȳ��ϼ���.\n") ;
    // }
    // else {
    //     printf("������ �ƴմϴ�.\n");
    // }

    // int score = 100;
    // if (score >= 90) {
    //     printf("A\n");
    // }
    // else if (score >= 80) {
    //     printf("B\n");
    // }
    // else if (score >= 70) {
    //     printf("c\n");
    // }
    // else {
    //     printf("F\n");
    // }

    // switch ��
    // int menu;
    // scanf("%d", &menu);

    // switch (menu) {
    // case 1:
    //     printf("�޴�1 ����\n");
    //     break;
    // case 2:
    //     printf("�޴�2 ����\n");
    //     break;
    // case 3:
    //     printf("�޴�3 ����\n");
    //     break;
    // default:
    //     printf("�߸��� �����Դϴ�.\n");
    // }

    // �ݺ���
    // while ��

    // int i = 1;
    // while (i <= 5) {
    //     printf("%d ", i);
    //     i++;
    // }

    // do - while��
    // int num = 0;
    // do {
    //     printf("�� ���� ��µ�!\n");
    // } while (num == 1);

    // for ��
    // for (int j = 0; j < 10; ++j) {
    //     printf("%d ", j);
    // }
    // for( ; ; )

    // int result = 0;
    // for (int j = 0; j < 10; ++j) {
    //     printf("%d", j);
    //     result += 2;
    //     if (result >= 10) {
    //         break;
    //     }
    // }

    // for (int i = 0; i < 10; ++i) {

    //     for (int j = 0; j < 10; ++j) {
    //         if () {
    //             break;
    //         }
    //     }
    // }

    // �ݺ��� ����
    // break : �ݺ��� ��� ����
    // continue : �Ʒ� �ڵ�� �ǳʶٰ�, ���� �ݺ����� �Ѿ
    return 0;
}