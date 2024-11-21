import re

# --- 1. File Reading ---
# Handles reading input file, splitting it into lines, and filtering empty lines
def read_file(filename):
    try:
        # Open the file and read its content
        with open(filename, "r") as f:
            x = f.read()

        # Split the content into lines and filter out empty lines
        req_list = x.split("\n")
        req_list = [i for i in req_list if i != ""]

        return req_list

    except FileNotFoundError:
        # Handle file not found error
        print(f"File {filename} not found.")
        return []

    except IOError:
        # Handle other I/O errors
        print(f"Error reading file {filename}.")
        return []

# --- 2. Class Initialization ---
# Handles initialization of the fullcode class, regex patterns, and module import flags
class fullcode:
    def __init__(self, code):
        self.code = code

        # Boolean flags for importing various modules
        self.a = False  # draw module
        self.b = False  # quiver module
        self.c = False  # rand module
        self.d = False  # output module
        self.e = False  # threedimensions module
        self.f = False  # clock module
        self.g = False  # math module

        # Regular expressions for pattern matching
        self.display_pattern = r'^display \.(.*?)\.'
        self.display_var_pattern = r'^display \|([^|]*)\|'
        self.display_list_pattern = r'^display \*([^|]*)\*'
        self.syntax_help = 0
        self.function_define = r'^function:([^|]*):\*([^|]*)\* \~\>'
        self.function_call = r'^run :([^:]*):\*([^*]*)\*'
        self.define_variable = r'^var:(.*?): = (.*?):(.*?):'
        self.define_list = r'^list:(.*?): = ([^|]*)'
        self.liststorage = r'^(.*?):([^|]*):'
        self.listcalling = r'^(.*?)<([^|]*)>'
        self.ender = ':break:'

    # --- 3. Error Handling ---
    # Returns a simple error message
    def err(self):
        return "err"

    # --- 4. Import Checking ---
    # Checks for various "bring all from ..." statements in the code
    def importing(self):
        if "bring all from draw" in self.code:
            self.a = True
        if "bring all from quiver" in self.code:
            self.b = True
        if "bring all from rand" in self.code:
            self.c = True
        if "bring all from output" in self.code:
            self.d = True
        if "bring all from threedimensions" in self.code:
            self.e = True
        if "bring all from clock" in self.code:
            self.f = True
        if "bring all from math" in self.code:
            self.g = True

    # --- 5. Quiver Logic ---
    # Processes code specifically when "bring all from quiver" is imported
    def quiver(self):
        # Call the importing method to check imports
        self.importing()

        # Initialize storage containers
        funcdisplaystore = []
        store = []
        varstore = {} 
        funcvarstore = {}
        funcliststore = []
        funcliststorage = {}
        liststore = []
        liststorage = {}
        parameterstore = {}
        funccodestore = {}

        # Process quiver-specific code
        if self.b:
            for i in self.code:
                # --- 5.1. Display Statements ---
                # Handles display syntax `display .item.`
                display = re.search(self.display_pattern, i)
                if display:
                    store.append(display.group(1))

                # --- 5.2. Variable Definition ---
                # Handles `var:name: = type:value:`
                variable = re.search(self.define_variable, i)
                if variable:
                    if variable.group(2) == "str":
                        varstore[variable.group(1)] = str(variable.group(3))
                    if variable.group(2) == "float":
                        varstore[variable.group(1)] = float(variable.group(3))
                    if variable.group(2) == "int":
                        varstore[variable.group(1)] = int(variable.group(3))

                # --- 5.3. Display Variables ---
                # Handles `display |var|`
                display_variable = re.search(self.display_var_pattern, i)
                if display_variable:
                    store.append(varstore.get(display_variable.group(1)))

                # --- 5.4. List Definition ---
                # Handles `list:name: = str:val, int:val`
                lists = re.search(self.define_list, i)
                if lists:
                    liststore.append(lists.group(2).split(', '))
                    listname = lists.group(1)
                    for item in liststore:
                        for a in item:
                            listchecker = re.search(self.liststorage, a)
                            itempos = int(item.index(a) + 1)
                            dictkeyname = [listname + '_' + str(itempos)]
                            if listchecker:
                                if listchecker.group(1) == "str":
                                    liststorage[str(dictkeyname[0])] = str(listchecker.group(2))
                                if listchecker.group(1) == "float":
                                    liststorage[str(dictkeyname[0])] = float(listchecker.group(2))
                                if listchecker.group(1) == "int":
                                    liststorage[str(dictkeyname[0])] = int(listchecker.group(2))

                # --- 5.5. Display Lists ---
                # Handles `display *list<index>*`
                display_lists = re.search(self.display_list_pattern, i)
                if display_lists:
                    listcallingsyntax = display_lists.group(1)
                    listcall = re.search(self.listcalling, listcallingsyntax)
                    if listcall:
                        listnamecheck = listcall.group(1)
                        listindexcheck = listcall.group(2)
                        dictnamecheck = [listnamecheck + '_' + listindexcheck]
                        store.append(liststorage.get(str(dictnamecheck[0])))

                # --- 5.6. Function Handling ---
                # Defines and calls functions using `function:name:*args* ~>` and `run :name:*args*`
                functiontest = re.search(self.function_define, i)
                functioncallcheck = re.search(self.function_call, i)
                if functiontest:
                    indexoffunction = self.code.index(f"function:{functiontest.group(1)}:*{functiontest.group(2)}* ~>")
                    funccodestore[functiontest.group(1)] = self.code[indexoffunction + 1:self.code.index(self.ender)]

                    if functioncallcheck and functioncallcheck.group(1) == functiontest.group(1):
                        for codes in funccodestore[functiontest.group(1)]:
                            codes = codes.replace("-> ", "")
                            funcdisplay = re.search(self.display_pattern, codes)
                            if funcdisplay:
                                funcdisplaystore.append(funcdisplay.group(1))

                            # Handle function-specific variable definitions
                            variablefunc = re.search(self.define_variable, codes)
                            if variablefunc:
                                if variablefunc.group(2) == "str":
                                    funcvarstore[variablefunc.group(1)] = str(variablefunc.group(3))
                                if variablefunc.group(2) == "float":
                                    funcvarstore[variablefunc.group(1)] = float(variablefunc.group(3))
                                if variablefunc.group(2) == "int":
                                    funcvarstore[variablefunc.group(1)] = int(variablefunc.group(3))

                            # Display variables in functions
                            display_variable_func = re.search(self.display_var_pattern, codes)
                            if display_variable_func:
                                funcdisplaystore.append(funcvarstore.get(display_variable_func.group(1)))

                            # Handle lists inside functions
                            listsfunc = re.search(self.define_list, codes)
                            if listsfunc:
                                funcliststore.append(listsfunc.group(2).split(', '))
                                funclistname = listsfunc.group(1)
                                for everyitem in funcliststore:
                                    for afunc in everyitem:
                                        funclistchecker = re.search(self.liststorage, afunc)
                                        itemposition = int(everyitem.index(afunc) + 1)
                                        funcdictkeyname = [funclistname + '_' + str(itemposition)]
                                        if funclistchecker:
                                            if funclistchecker.group(1) == "str":
                                                funcliststorage[str(funcdictkeyname[0])] = str(funclistchecker.group(2))
                                            if funclistchecker.group(1) == "float":
                                                funcliststorage[str(funcdictkeyname[0])] = float(funclistchecker.group(2))
                                            if funclistchecker.group(1) == "int":
                                                funcliststorage[str(funcdictkeyname[0])] = int(funclistchecker.group(2))

                            # Display lists inside functions
                            display_lists_func = re.search(self.display_list_pattern, codes)
                            if display_lists_func:
                                funclistcallingsyntax = display_lists_func.group(1)
                                funclistcall = re.search(self.listcalling, funclistcallingsyntax)
                                if funclistcall:
                                    funclistnamecheck = funclistcall.group(1)
                                    funclistindexcheck = funclistcall.group(2)
                                    funcdictnamecheck = [funclistnamecheck + '_' + funclistindexcheck]
                                    funcdisplaystore.append(funcliststorage.get(str(funcdictnamecheck[0])))

            return store, funcdisplaystore if functioncallcheck else store

    # --- 6. Rand Logic (Placeholder) ---
    def rand(self):
        if self.c:
            pass
        else:
            self.err()

    # --- 7. Output Logic (Placeholder) ---
    def output(self):
        if self.d:
            pass
        else:
            self.err()

    # --- 8. Clock Logic (Placeholder) ---
    def clock(self):
        if self.f:
            pass
        else:
            self.err()

    # --- 9. Math Logic (Placeholder) ---
    def math(self):
        if self.g:
            pass
        else:
            self.err()

    def __str__(self) -> str:
        return "Do not print the class"

# --- 10. Usage Example ---
# Read code from the file and execute
x = read_file("Code editor for coding language/language.txt")
sourcecode = fullcode(x)

# Test the code execution
result = sourcecode.quiver()
for i in result:
    print(i)
