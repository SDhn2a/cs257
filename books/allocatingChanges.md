# changes that need to be made
- change usage doc on one year input for between years
- need to specifiy in doc that incorrectly ordered year are fine or **remove that funcunality** or move to books.py
  - do with assert


 open usage.txt when help needed?
# changes that we should discuss
- handle folks with middle names diffrently?
  - and add a unit test
- In your “-h” function for the program, If you could find a way to move around the
order to get --sort_title and --sort_publication_year to be below the most
important flags (--search_...)
- You could see if you could find a way to take into account the authors with three
names?
- Parse_book_authors feels a little cumbersome to read (with the constant values) but it does feel like a problem that requires some hard coding. Maybe with some very small comments in this section that explain conceptually how it works would be easier to scan but ok overall.
- Comments are really good most of the time, sometime feel redundant
- I am not totally sure why the date doesn’t work entirely as expected from the command line but it is something to look into
- I am not sure how sys.argv is used alongside argparse -- admittedly this mainly stems from my own lack of knowledge
- (-)In books.py, instead of hardcoding CSV_SOURCE as the books1.csv file, you could maybe include the file to read as a command to make it possible to look at other files. This is just quibbling though, it works fine as is.
- The comments denoting what each method does are generally helpful. However, the # comments in your code are a little bit excessive. For the most part, they are just repeating information that your variable names already cover, and they add clutter to the code.
- I am confused by your sorting method. This might just be because I have never seen this syntax before. I think it works, but it is really confusing to me. 
- It is also unclear to me if your books method handles the case where they try to type something other than ‘title’ or ‘year’ for the sort term
# changes that we are not making
