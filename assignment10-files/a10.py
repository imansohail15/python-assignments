## IMPORTS GO HERE
import os
## END OF IMPORTS



### YOUR CODE FOR line_count() FUNCTION GOES HERE ###
def line_count(directory,filename,strip_lines=False):
    filepath=os.path.join(directory,filename)
    with open(filepath,'r')as f:
        lines=f.readlines()
    if strip_lines:
        count=0
        for line in lines:
            if line.strip():
                count +=1
            return count
        else:
            return len(lines)
#### End OF MARKER



### YOUR CODE FOR character_count() FUNCTION GOES HERE ###
def character_count(directory,filename,strip_spaces=False):
    filepath=os.path.join(directory,filename)
    with open(filepath,'r') as f:
        content = f.read()
    if strip_spaces:
        total_chars=0
        for char in content:
            if not char.isspace():
                total_chars +=1
        return total_chars
    else:
        return len(content)
#### End OF MARKER



### YOUR CODE FOR move_lines() FUNCTION GOES HERE ###
def move_lines(src_filename,dest_filename,n):
    with open(src_filename,'r') as src_file:
        lines=src_file.readlines()
    lines_to_move=lines[:n]
    remaining_lines=lines[n:]
    with open(dest_filename,'w') as dest_file:
        dest_file.writelines(lines_to_move)
    with open(src_filename,'w') as src_file:
        src_file.writelines(remaining_lines)
        
#### End OF MARKER



if __name__ == '__main__':
    print (line_count('.', 'essay.txt'))
    print (line_count('.', 'essay.txt', True))

    print (character_count('.', 'essay.txt'))
    print (character_count('.', 'essay.txt', True))

    move_lines('essay.txt', 'out.txt', 3)

    pass
