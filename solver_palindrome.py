from pwn import *


def copy(lst):
    lst2 = []
    for i in lst:
        lst2.append(i)

    return lst2


def is_palindrome(s):
    head = 0
    tail = len(s) - 1
    while(head < tail):
        if(s[head] != s[tail]):
            return False
        head += 1
        tail -= 1

    # print(s)
    return True


def get_palindromes_set(lst):
    palin_set = set()
    for e in lst:
        if is_palindrome(e):
            palin_set.add(e)
    return palin_set


def get_palindromes_num(lst):
    count = 0
    length = len(lst)

    for i in range(0, length):
        elm = lst[i]        
        rest = lst[i+1:length]

        if len(rest) != 0:
            head_list = [is_palindrome(elm + e) for e in rest]
            last_list = [is_palindrome(e + elm) for e in rest]
            count += head_list.count(True) + last_list.count(True)

        if is_palindrome(elm + elm):
            count += 1

    return count

host = 'ppc1.chal.ctf.westerns.tokyo'
port = '8765'
p = remote(host, port)

log.info(p.recvuntil('----- START -----\n'))
for _ in range(50):
    log.info(p.recvuntil('\n'))
    log.info("num:" + p.recvuntil('\n'))    
    words = p.recvuntil('\n')
    log.info(words)

    words = words.strip().split(" ")
    ans = get_palindromes_num(words)
    log.info(str(ans))
    p.sendline(str(ans))
    log.info(p.recvuntil('\n'))
    p.recvuntil('\n')

p.interactive()
