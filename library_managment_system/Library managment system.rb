Library managment system



============ fields
student
  id
  name
  gmail
  password
  branch id
  penalty

Books
------------------------
  id
  name
  author
  branch id
  book_count

branch
----------------------
  id
  name

Librarian 
---------------------
  id
  name
  gmail
  password

============== function
student
-------------------
  /student/login                == gmail, password
  /student/register             == name, gmail, branch id, password

  /student/isuued_books         == gmail
  /student/display_books
  /student/borrow_book          == gmail, branch, book id
  /student/return_book          == gmail, book id

  /student/see_penalty          == gmail

librarian
-----------------------------
  /librarian/login                == email, password
  /librarian/register             == name, email, password


  /librarian/display_books        
  /librarian/insert_book          == [name, author, branch, book_count]
  /librarian/update_book          == book id, [name, author, branch, book_count]
  /librarian/delete_book          == book id
  
  /librarian/display_branch    
  /librarian/insert_branch        == gmail, [branch name]
  /librarian/update_branch        == gmail, branch id, [branch name]
  /librarian/delete_branch        == gmail, branch id

  /librarian/see_penalty          == gmail, student gmail
  /librarian/clear_penalty        == gmail, student gmail, amount
  



