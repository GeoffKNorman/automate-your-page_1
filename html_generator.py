EXAMPLE_LIST_OF_CONCEPTS = [ ['Previous Examples of Code', 
'''In begining this second project, I had an understanding of for loops, while loops, string indexing and concatenation, but I had no idea how we were going to produce HTML tags around our text.  
I was relieved to know that we would learn something useful to do this but I was horrified by the first exercises where we had to perform string matching to slice apart a giant block of text to create our notes like so:
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = + \'\'\'
<div class="concept">
    <div class="concept-title">
        \'\'\' + concept_title
    html_text_2 = \'\'\'
    </div>
    <div class="concept-description">
        \'\'\' + concept_description
    html_text_3 = \'\'\'
    </div>
</div>\'\'\'
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

TEST_TEXT = \"\"\"TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.
TITLE: Python
DESCRIPTION: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true.\"\"\"


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html
''', "lesson-4-1"],
                             ['A better way using Lists!', '''Using lists, we learned how to take less steps in separating out our content and I realized I could automate the generation of the html for my sublists by adding an extra list item after my content.  
                             Being very lazy on my part, I decided just to copy over the output from my python file instead of pasting in all the previous content into the python list (because that would have taken forever and I would rather learn sometehing new) and make a few tweaks once I had placed my content safely in my HTML document.  
                             A few tweaks here and there, and realizing that I hadn't added an h2 tag to beginning of this new section, nor had I thought to nest my content even further to include headers and the section heading around my content... I made the changes manually to save time and submit my project and move on.  

                             Really glad to learn about nesting lists and calling individual elements through [] indexing and for loops. <p> Here is the better way of using these procedures to wrap our notes in HTML tags:</p> 

def generate_concept_HTML(concept_title, concept_description, lesson_id):
    html_text_1 = \'\'\'
<div class="concept">
    <div class="concept-title",\'\'\' + "<id=" + lesson_id + ">"+ concept_title 
    html_text_2 = \'\'\'
    </div>
    <div class="concept-description">
        \'\'\' + concept_description
    html_text_3 = \'\''\
    </div>
</div>\'\'\'
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    lesson_id = concept[2]
    return generate_concept_HTML(concept_title, concept_description, lesson_id)

# This is an example of what a list of concepts might look like.

def TOCmaker(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    lesson_id = concept[2]
    list_html = \'\'\'
    <li><a href="#\'\'\' lesson_id + \'\'\'">\'\'\' + concept_title + \'\'\'</a></li>\'\'\'
    return list_html


# This is the function you will write.
def make_HTML_for_many_concepts(list_of_concepts):
    list_of_TOC = ''
    many_HTML = ''
    for concept in list_of_concepts:
        many_HTML += make_HTML(concept)
        list_of_TOC += TOCmaker(concept)


    return many_HTML
    return list_of_TOC

# This is an example of what a list of concepts might look like.
EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language', lesson_id=lesson-4-1],
                             ['For Loop', 'For Loops allow you to iterate over lists'lesson_id=lesson-4-2],
                             ['Lists', 'Lists are sequences of data'lesson_id=lesson-4-3] ]

# This is the function you will write.
def make_HTML_for_many_concepts(list_of_concepts):
    many_HTML = ''
    for i in list_of_concepts:
        many_HTML += make_HTML(i)
    return many_HTML
        
    # write code here that generates the appropriate HTML
    # for a list of concepts.

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
''',"lesson-4-2"],["Once and for all...please stop failing me on my notes - I'm really here to learn how to code not take proper academic notes",
'''
      <p>A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.</p>
      <p>As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own functions. These functions are called <i>user-defined functions.</i></p>
      <h2>Defining a Function</h2>
      <p>You can define functions to provide the required functionality. Here are simple rules to define a function in Python.</p>
      <ul class="list">
      <li><p>Function blocks begin with the keyword <b>def</b> followed by the function name and parentheses ( ( ) ).</p></li>
      <li><p>Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.</p></li>
      <li><p>The first statement of a function can be an optional statement - the documentation string of the function or <i>docstring</i>.</p></li>
      <li><p>The code block within every function starts with a colon (:) and is indented.</p></li>
      <li><p>The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.</p></li>
      </ul>
      <h2>Syntax</h2>
      <pre class="prettyprint notranslate">
      def functionname( parameters ):
         "function_docstring"
         function_suite
         return [expression]
      </pre>
      <p>By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.</p>
      <h2>Example</h2>
      <p>The following function takes a string as input parameter and prints it on standard screen.</p>
      <pre class="prettyprint notranslate">
      def printme( str ):
         "This prints a passed string into this function"
         print str
         return
      </pre>
      <h2>Calling a Function</h2>
      <p>Defining a function only gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code.</p>
      <p>Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from the Python prompt. Following is the example to call printme() function &minus;</p>
      <pre class="prettyprint notranslate tryit">
      #!/usr/bin/python

      # Function definition is here
      def printme( str ):
         "This prints a passed string into this function"
         print str;
         return;

      # Now you can call printme function
      printme("I'm first call to user defined function!");
      printme("Again second call to the same function");
      </pre>
      <p>When the above code is executed, it produces the following result &minus;</p>
      <pre class="prettyprint notranslate">
      I'm first call to user defined function!
      Again second call to the same function
      </pre>
      <h2>Pass by reference vs value</h2>
      <p>All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter refers to within a function, the change also reflects back in the calling function. For example &minus;</p>
      <pre class="prettyprint notranslate tryit">
      #!/usr/bin/python

      # Function definition is here
      def changeme( mylist ):
         "This changes a passed list into this function"
         mylist.append([1,2,3,4]);
         print "Values inside the function: ", mylist
         return

      # Now you can call changeme function
      mylist = [10,20,30];
      changeme( mylist );
      print "Values outside the function: ", mylist
      </pre>
      <p>Here, we are maintaining reference of the passed object and appending values in the same object. So, this would produce the following result &minus;</p>
      <pre class="prettyprint notranslate">
      Values inside the function:  [10, 20, 30, [1, 2, 3, 4]]
      Values outside the function:  [10, 20, 30, [1, 2, 3, 4]]
      </pre>
      <p>There is one more example where argument is being passed by reference and the reference is being overwritten inside the called function.</p>
      <pre class="prettyprint notranslate tryit">
      #!/usr/bin/python

      # Function definition is here
      def changeme( mylist ):
         "This changes a passed list into this function"
         mylist = [1,2,3,4]; # This would assig new reference in mylist
         print "Values inside the function: ", mylist
         return

      # Now you can call changeme function
      mylist = [10,20,30];
      changeme( mylist );
      print "Values outside the function: ", mylist
      </pre>
      <p>The parameter <i>mylist</i> is local to the function changeme. Changing mylist within the function does not affect <i>mylist</i>. The function accomplishes nothing and finally this would produce the following result:</p>
      <pre class="prettyprint notranslate">
      Values inside the function:  [1, 2, 3, 4]
      Values outside the function:  [10, 20, 30]
      </pre>
      <h2>Function Arguments</h2>
      <p>You can call a function by using the following types of formal arguments:</p>
      <ul class="list">
      <li><p>Required arguments</p></li>
      <li><p>Keyword arguments</p></li>
      <li><p>Default arguments</p></li>
      <li><p>Variable-length arguments</p></li>
      </ul>
      <h2>Required arguments</h2>
      <p>Required arguments are the arguments passed to a function in correct positional order. Here, the number of arguments in the function call should match exactly with the function definition.</p>
      <p>To call the function <i>printme()</i>, you definitely need to pass one argument, otherwise it gives a syntax error as follows &minus;</p>
      <pre class="prettyprint notranslate tryit">
      #!/usr/bin/python

      # Function definition is here
      def printme( str ):
         "This prints a passed string into this function"
         print str;
         return;

      # Now you can call printme function
      printme();
      </pre>
      <p>When the above code is  executed, it produces the following result:</p>
      <pre class="prettyprint notranslate">
      Traceback (most recent call last):
        File "test.py", line 11, in &lt;module&gt;
          printme();
      TypeError: printme() takes exactly 1 argument (0 given)
      </pre>
      <h2>Keyword arguments</h2>
      <p>Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.</p>
      <p>This allows you to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the values with parameters. You can also make keyword calls to the <i>printme()</i> function in the following ways &minus;</p>
      <pre class="prettyprint notranslate tryit">
      #!/usr/bin/python

      # Function definition is here
      def printme( str ):
         "This prints a passed string into this function"
         print str;
         return;

      # Now you can call printme function
      printme( str = "My string");
      </pre>
      <p>When the above code is  executed, it produces the following result &minus;</p>
      <pre class="prettyprint notranslate">
      My string
      </pre>
      <p>The following example gives more clear picture. Note that the order of parameters does not matter.</p>
      <pre class="prettyprint notranslate tryit">
      #!/usr/bin/python

      # Function definition is here
      def printinfo( name, age ):
         "This prints a passed info into this function"
         print "Name: ", name;
         print "Age ", age;
         return;

      # Now you can call printinfo function
      printinfo( age=50, name="miki" );
      </pre>
      <p>When the above code is  executed, it produces the following result &minus;</p>
      <pre class="prettyprint notranslate">
      Name:  miki
      Age  50
      </pre>
      <h2>Default arguments</h2>
      <p>A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument. The following example gives an idea on default arguments, it prints default age if it is not passed &minus;</p>
      <pre class="prettyprint notranslate tryit">
      #!/usr/bin/python

      # Function definition is here
      def printinfo( name, age = 35 ):
         "This prints a passed info into this function"
         print "Name: ", name;
         print "Age ", age;
         return;

      # Now you can call printinfo function
      printinfo( age=50, name="miki" );
      printinfo( name="miki" );
      </pre>
      <p>When the above code is  executed, it produces the following result &minus;</p>
      <pre class="prettyprint notranslate">
      Name:  miki
      Age  50
      Name:  miki
      Age  35
      </pre>
      <h2>Variable-length arguments</h2>
      <p>You may need to process a function for more arguments than you specified while defining the function. These arguments are called <i>variable-length</i> arguments and are not named in the function definition, unlike required and default arguments.</p>
      <p>Syntax for a function with non-keyword variable arguments is this &minus;</p>
      <pre class="prettyprint notranslate">
      def functionname([formal_args,] *var_args_tuple ):
         "function_docstring"
         function_suite
         return [expression]
      </pre>
      <p>An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments. This tuple remains empty if no additional arguments are specified during the function call. Following is a simple example &minus;</p>
      <pre class="prettyprint notranslate tryit">
      #!/usr/bin/python

      # Function definition is here
      def printinfo( arg1, *vartuple ):
         "This prints a variable passed arguments"
         print "Output is: "
         print arg1
         for var in vartuple:
            print var
         return;

      # Now you can call printinfo function
      printinfo( 10 );
      printinfo( 70, 60, 50 );
      </pre>
      <p>When the above code is  executed, it produces the following result &minus;</p>
      <pre class="prettyprint notranslate">
      Output is:
      10
      Output is:
      70
      60
      50
      </pre>
      <h2>The <i>Anonymous</i> Functions</h2>
      <p>These functions are called anonymous because they are not declared in the standard manner by using the <i>def</i> keyword. You can use the <i>lambda</i> keyword to create small anonymous functions.</p>
      <ul class="list">
      <li><p>Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.</p></li>
      <li><p>An anonymous function cannot be a direct call to print because lambda requires an expression</p></li>
      <li><p>Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.</p></li>
      <li><p>Although it appears that lambda's are a one-line version of a function, they are not equivalent to inline statements in C or C++, whose purpose is by passing function stack allocation during invocation for performance reasons.</p></li>
      </ul>
      <h2>Syntax</h2>
      <p>The syntax of <i>lambda</i> functions contains only a single statement, which is as follows &minus;</p>
      <pre class="prettyprint notranslate">
      lambda [arg1 [,arg2,.....argn]]:expression
      </pre>
      <p>Following is the example to show how <i>lambda</i> form of function works &minus;</p>
      <pre class="prettyprint notranslate tryit">
      #!/usr/bin/python

      # Function definition is here
      sum = lambda arg1, arg2: arg1 + arg2;

       

      # Now you can call sum as a function
      print "Value of total : ", sum( 10, 20 )
      print "Value of total : ", sum( 20, 20 )
      </pre>
      <p>When the above code is  executed, it produces the following result &minus;</p>
      <pre class="prettyprint notranslate">
      Value of total :  30
      Value of total :  40
      </pre>
      <h2>The <i>return</i> Statement</h2>
      <p>The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.</p>
      <p>All the above examples are not returning any value. You can return a value from a function as follows &minus;</p>
      <pre class="prettyprint notranslate tryit">
      #!/usr/bin/python

      # Function definition is here
      def sum( arg1, arg2 ):
         # Add both the parameters and return them."
         total = arg1 + arg2
         print "Inside the function : ", total
         return total;

      # Now you can call sum function
      total = sum( 10, 20 );
      print "Outside the function : ", total 
      </pre>
      <p>When the above code is  executed, it produces the following result &minus;</p>
      <pre class="prettyprint notranslate">
      Inside the function :  30
      Outside the function :  30
      </pre>
      <h2>Scope of Variables</h2>
      <p>All variables in a program may not be accessible at all locations in that program. This depends on where you have declared a variable.</p>
      <p>The scope of a variable determines the portion of the program where you can access a particular identifier. There are two basic scopes of variables in Python  &minus;</p>
      <ul class="list">
      <li><p>Global variables</p></li>
      <li><p>Local variables</p></li>
      </ul>
      <h2>Global vs. Local variables</h2>
      <p>Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.</p>
      <p>This means that local variables can be accessed only inside the function in which they are declared, whereas global variables can be accessed throughout the program body by all functions. When you call a function, the variables declared inside it are brought into scope. Following is a simple example &minus;</p>
      <pre class="prettyprint notranslate tryit">
      #!/usr/bin/python

      total = 0; # This is global variable.
      # Function definition is here
      def sum( arg1, arg2 ):
         # Add both the parameters and return them."
         total = arg1 + arg2; # Here total is local variable.
         print "Inside the function local total : ", total
         return total;

      # Now you can call sum function
      sum( 10, 20 );
      print "Outside the function global total : ", total 
      </pre>
      <p>When the above code is  executed, it produces the following result &minus;</p>
      <pre class="prettyprint notranslate">
      Inside the function local total :  30
      Outside the function global total :  0
      </pre>
      
''',"lesson-4-3"]]

def generate_concept_HTML(concept_title, concept_description, lesson_id):
    concept_description = concept_description.replace('<', ' &lt; ')
    concept_description = concept_description.replace('>', ' &gt; ')
    concept_description = concept_description.replace('\n', '<br />')

    html_text_1 = '''
<div class="concept">
    <div class="concept-title "''' + ''' id="''' + lesson_id + '''">'''+ concept_title 
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    lesson_id = concept[2]
    return generate_concept_HTML(concept_title, concept_description, lesson_id)

# This is an example of what a list of concepts might look like.

def TOCmaker(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    lesson_id = concept[2]
    list_html = '''
    <li><a href="#''' + lesson_id + '''">''' + concept_title + '''</a></li>'''
    return list_html


# This is the function you will write.
def make_HTML_for_many_concepts(list_of_concepts):
    list_of_TOC = ''
    many_HTML = ''
    for concept in list_of_concepts:
        many_HTML += make_HTML(concept)
        list_of_TOC += TOCmaker(concept)
    return many_HTML

def make_TOC_for_many_concepts(list_of_concepts):
    list_of_TOC = ''
    for concept in list_of_concepts:
        list_of_TOC += TOCmaker(concept)
    return list_of_TOC


    # write code here that generates the appropriate HTML
    # for a list of concepts.

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
print make_TOC_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)

