this_is_string = "Hi there!"
the_same_string = 'Hi there!'
this_is_string == the_same_string  # True

#====================================================================================
text = """This is first line
And second line
Last third line"""

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''

print(text)
print("*" * 20)
print(song)
#====================================================================================
one_line_text = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
#====================================================================================
one_line_text = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."
#====================================================================================
multi_line_text = (
    "Textual data in Python is handled with str objects, "
    "or strings. Strings are immutable sequences of Unicode "
    "code points. String literals are written in a variety "
    "of ways: single quotes, double quotes, triple quoted."
)
#====================================================================================
"""
SQL запити до бази даних:
"""
query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")
print(query)
#====================================================================================
print("Hello\nWorld")
print("Hello\tWorld")
print("C:\\new_folder\\test.txt")
print("She said: \"Hello!\"")       
print('It\'s a sunny day!')
#====================================================================================
print("Hello my little\rsister")
print("Hello my little\bbrother")
print("Hello my little\ffriend")    
print("Hello my little\vnation")
print("Hello my little\atown")
#====================================================================================
print('It\'s a beautiful day')
print("He said, \"Hello\"")
print("This is the first line.\nThis is the second line.")
print("Column1\tColumn2\tColumn3")  
#====================================================================================
