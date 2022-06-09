# Backspace_String_Compare
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_mod = ""
        T_mod = ""
        for i in range(len(S)):
            if S[i] =="#": S_mod = S_mod[:len(S_mod)-1]
            else: S_mod = S_mod + S[i]
                
        for i in range(len(T)):
            if T[i] =="#": T_mod = T_mod[:len(T_mod)-1]
            else: T_mod = T_mod + T[i]
                
        if S_mod == T_mod: return True
        else: return False
                
