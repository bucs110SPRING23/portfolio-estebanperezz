class StringUtility:
    def __init__ (self,string):
        self.string = string 
    def __str__(self):
        string_as_str = str(self.string)
        return string_as_str

    def vowels(self):
        vowels = 'aeiouAEIOU'
        num_vowels = 0
        for _ in self.string:
            if _ in vowels:
                num_vowels += 1
        self.num = num_vowels
        if self.num <5:
            return str(self.num)
        else:
            return str("many")
    def bothEnds(self):

        if len(self.string)<=2:
            return ""
        else:
            return self.string[:2] + self.string[-2:]

    def fixStart(self):
        if len(self.string)<=1:
            return self.string
        else:
            char1 = self.string[0]
            fullstring = self.string[1:]
            newstring = char1 + fullstring.replace(char1,"*")
            return newstring
    def asciiSum(self):
        total = 0 
        for char in self.string:
            total +=ord(char)
        return total
    def cipher(self):
        shift = len(self.string)
        newstring = ""
        for _ in self.string:
            if _.isalpha():
                if _.isupper():
                    coded_=chr(ord(_)-65 +shift) % 26 + 65
                else:
                    coded_ = chr(ord(_) - 97) % 26 +97 
            else: coded_ = _ 
            newstring += coded_
            return newstring



        
        

    

