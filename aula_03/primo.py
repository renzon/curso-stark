def eh_primo(n: int) -> bool:
    for i in range(2, n):
        resto = n % i
        if resto == 0:
            return False
    return True


print(29, eh_primo(29))
print(30, eh_primo(30))