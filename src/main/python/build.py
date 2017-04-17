import jinja2
import html

ORACLE_RESERVED_WORDS = [
    "ACCESS","ELSE","MODIFY","START", "ADD","EXCLUSIVE","NOAUDIT","SELECT",
    "ALL","EXISTS","NOCOMPRESS","SESSION", "ALTER","FILE","NOT","SET",
    "AND","FLOAT","NOTFOUND","SHARE", "ANY","FOR","NOWAIT","SIZE",
    "ARRAYLEN","FROM","NULL","SMALLINT", "AS","GRANT","NUMBER","SQLBUF",
    "ASC","GROUP","OF","SUCCESSFUL", "AUDIT","HAVING","OFFLINE","SYNONYM",
    "BETWEEN","IDENTIFIED","ON","SYSDATE", "BY","IMMEDIATE","ONLINE","TABLE",
    "CHAR","IN","OPTION","THEN", "CHECK","INCREMENT","OR","TO",
    "CLUSTER","INDEX","ORDER","TRIGGER", "COLUMN","INITIAL","PCTFREE","UID",
    "COMMENT","INSERT","PRIOR","UNION", "COMPRESS","INTEGER","PRIVILEGES","UNIQUE",
    "CONNECT","INTERSECT","PUBLIC","UPDATE", "CREATE","INTO","RAW","USER",
    "CURRENT","IS","RENAME","VALIDATE", "DATE","LEVEL","RESOURCE","VALUES",
    "DECIMAL","LIKE","REVOKE","VARCHAR", "DEFAULT","LOCK","ROW",
    "DELETE","LONG","ROWID","VIEW", "DESC","MAXEXTENTS","ROWLABEL","WHENEVER",
    "DISTINCT","MINUS","ROWNUM","WHERE", "DROP","MODE","ROWS","WITH"
]

ORACLE_KEYWORDS = [
    "ADMIN", "AFTER", "ALLOCATE", "ANALYZE", "ARCHIVE", "ARCHIVELOG", "AUTHORIZATION", "AVG", "BACKUP",
    "BECOME", "BEFORE", "BEGIN", "BLOCK", "BODY", "CACHE", "CANCEL", "CASCADE", "CHANGE",
    "CHARACTER", "CHECKPOINT", "CLOSE", "COBOL", "COMMIT", "COMPILE", "CONSTRAINT", "CONSTRAINTS", "CONTENTS",
    "CONTINUE", "CONTROLFILE", "COUNT", "CURSOR", "CYCLE", "DATABASE", "DATAFILE", "DBA", "DEC",
    "DECLARE", "DISABLE", "DISMOUNT", "DOUBLE", "DUMP", "EACH", "ENABLE", "END", "ESCAPE",
    "EVENTS", "EXCEPT", "EXCEPTIONS", "EXEC", "EXECUTE", "EXPLAIN", "EXTENT", "EXTERNALLY", "FETCH",
    "FLUSH", "FORCE", "FOREIGN", "FORTRAN", "FOUND", "FREELIST", "FREELISTS", "FUNCTION", "GO", "GOTO",
    "GROUPS", "INCLUDING", "INDICATOR", "INITRANS", "INSTANCE", "INT", "KEY", "LANGUAGE", "LAYER", "LINK",
    "LISTS", "LOGFILE", "MANAGE", "MANUAL", "MAX", "MAXDATAFILES", "MAXINSTANCES", "MAXLOGFILES", "MAXLOGHISTORY",
    "MAXLOGMEMBERS", "MAXTRANS", "MAXVALUE", "MIN", "MINEXTENTS", "MINVALUE", "MODULE", "MOUNT", "NEW", "NEXT",
    "NOARCHIVELOG", "NOCACHE", "NOCYCLE", "NOMAXVALUE", "NOMINVALUE", "NONE", "NOORDER", "NORESETLOGS", "NORMAL",
    "NOSORT", "NUMERIC", "OFF", "OLD", "ONLY", "OPEN", "OPTIMAL", "OWN", "PACKAGE", "PARALLEL", "PCTINCREASE",
    "PCTUSED", "PLAN", "PLI", "PRECISION", "PRIMARY", "PRIVATE", "PROCEDURE",
    "PROFILE","SAVEPOINT","SQLSTATE","TRACING","QUOTA","SCHEMA","STATEMENT_ID","TRANSACTION","READ","SCN",
    "STATISTICS","TRIGGERS","REAL","SECTION","STOP","TRUNCATE","RECOVER","SEGMENT","STORAGE","UNDER",
    "REFERENCES","SEQUENCE","SUM","UNLIMITED","REFERENCING","SHARED","SWITCH","UNTIL","RESETLOGS",
    "SNAPSHOT","SYSTEM","USE","RESTRICTED","SOME","TABLES","USING","REUSE","SORT","TABLESPACE",
    "WHEN","ROLE","SQL","TEMPORARY","WRITE","ROLES","SQLCODE","THREAD","WORK","ROLLBACK","SQLERROR","TIME","REPLACE"
]

ORACLE_PLSQL_RESERVED_WORDS = [
    "ABORT","BETWEEN","CRASH","DIGITS","ACCEPT","BINARY_INTEGER",
    "CREATE","DISPOSE","ACCESS","BODY","CURRENT","DISTINCT","ADD","BOOLEAN","CURRVAL","DO","ALL","BY",
    "CURSOR","DROP","ALTER","CASE","DATABASE","ELSE","AND","CHAR","DATA_BASE","ELSIF","ANY","CHAR_BASE",
    "DATE","END","ARRAY","CHECK","DBA","ENTRY","ARRAYLEN","CLOSE","DEBUGOFF","EXCEPTION","AS",
    "CLUSTER","DEBUGON","EXCEPTION_INIT","ASC","CLUSTERS","DECLARE","EXISTS","ASSERT","COLAUTH","DECIMAL",
    "EXIT","COLUMNS","DEFAULT","FALSE","AT","COMMIT","DEFINITION","FETCH","AUTHORIZATION",
    "COMPRESS","DELAY","FLOAT","AVG","CONNECT","DELETE","FOR","BASE_TABLE","CONSTANT","DELTA","FORM",
    "BEGIN","COUNT","DESC","FROM","FUNCTION","NEW","RELEASE","SUM","GENERIC","NEXTVAL","REMR","TABAUTH",
    "GOTO","NOCOMPRESS","RENAME","TABLE","GRANT","NOT","RESOURCE","TABLES","GROUP","NULL","RETURN",
    "TASK","HAVING","NUMBER","REVERSE","TERMINATE","IDENTIFIED","NUMBER_BASE","REVOKE","THEN","IF","OF",
    "ROLLBACK","TO","IN","ON","ROWID","TRUE","INDEX","OPEN","ROWLABEL","TYPE","INDEXES","OPTION","ROWNUM",
    "UNION","INDICATOR","OR","ROWTYPE","UNIQUE","INSERT","ORDER","RUN","UPDATE","INTEGER","OTHERS",
    "SAVEPOINT","USE","INTERSECT","OUT","SCHEMA","VALUES","INTO","PACKAGE","SELECT","VARCHAR","IS","PARTITION",
    "SEPARATE","LEVEL","PCTFREE","SET","VARIANCE","LIKE","POSITIVE","SIZE","VIEW","LIMITED",
    "PRAGMA","SMALLINT","VIEWS","LOOP","PRIOR","SPACE","WHEN","MAX","PRIVATE","SQL","WHERE","MIN","PROCEDURE",
    "SQLCODE","WHILE","MINUS","PUBLIC","SQLERRM","WITH","MLSLABEL","RAISE","START","WORK","MOD","RANGE",
    "STATEMENT","XOR","MODE","REAL","STDDEV","NATURAL","RECORD","SUBTYPE","NOCOPY",
    "CONSTRUCTOR", "SELF", "RESULT", "MEMBER", "STATIC"
]

ORACLE_TYPES = ["\\s+".join(i.split()) for i in [
    "ANYDATA", "ANYTYPE", "BINARY_DOUBLE", "BINARY_FLOAT", "BLOB", "BOOLEAN", "CHAR", "CLOB", "DATE", "DSINTERVAL_UNCONSTRAINED",
    "INTEGER", "INTERVAL DAY TO SECOND", "LONG", "NCHAR", "NUMBER", "PLS_INTEGER", "RAW", "SIMPLE_INTEGER",
    "SYS_REFCURSOR", "TIMESTAMP", "TIMESTAMP WITH LOCAL TIME ZONE", "TIMESTAMP WITH TIME ZONE",
    "TIMESTAMP_LTZ_UNCONSTRAINED", "TIMESTAMP_TZ_UNCONSTRAINED", "TIMESTAMP_UNCONSTRAINED", "VARCHAR2"
]]

ORACLE_BUILTIN_FUNCTIONS = [
    "ABS", "ACOS", "ADD_MONTHS", "ASCII", "ASCIISTR", "ASIN", "ATAN", "ATAN2", "AVG", "BFILENAME", "BIN_TO_NUM", "BITAND",
    "CARDINALITY", "CAST", "CEIL", "CHARTOROWID", "CHR", "COALESCE", "COMPOSE", "CONCAT", "CONVERT", "CORR", "COS", "COSH",
    "COUNT", "COVAR_POP", "COVAR_SAMP", "CUME_DIST", "CURRENT_DATE", "CURRENT_TIMESTAMP", "DBTIMEZONE", "DECODE", "DECOMPOSE",
    "DENSE_RANK", "DUMP", "EMPTY_BLOB", "EMPTY_CLOB", "EXP", "EXTRACT", "FIRST_VALUE", "FLOOR",
    "FROM_TZ", "GREATEST", "GROUP_ID", "HEXTORAW", "INITCAP", "INSTR", "INSTR2", "INSTR4", "INSTRB", "INSTRC", "LAG", "LAST_DAY",
    "LAST_VALUE", "LEAD", "LEAST", "LENGTH", "LENGTH2", "LENGTH4", "LENGTHB", "LENGTHC", "LISTAGG", "LN", "LNNVL", "LOCALTIMESTAMP",
    "LOG", "LOWER", "LPAD", "LTRIM", "MAX", "MEDIAN", "MIN", "MOD", "MONTHS_BETWEEN", "NANVL", "NCHR", "NEW_TIME", "NEXT_DAY",
    "NTH_VALUE", "NULLIF", "NUMTODSINTERVAL",
    "NUMTOYMINTERVAL","NVL","NVL2","POWER","RANK","RAWTOHEX","REGEXP_COUNT","REGEXP_INSTR","REGEXP_REPLACE","REGEXP_SUBSTR",
    "REMAINDER","REPLACE","ROUND","ROWNUM","RPAD","RTRIM","SESSIONTIMEZONE","SIGN","SIN","SINH","SOUNDEX","SQLCODE","SQLERRM",
    "SQRT","STDDEV","SUBSTR","SUM","SYS_CONTEXT","SYSDATE","SYSTIMESTAMP","TAN","TANH","TO_CHAR","TO_CLOB","TO_DATE","TO_DSINTERVAL",
    "TO_LOB", "TO_MULTI_BYTE", "TO_NCLOB","TO_NUMBER","TO_SINGLE_BYTE","TO_TIMESTAMP","TO_TIMESTAMP_TZ","TO_YMINTERVAL","TRANSLATE",
    "TRIM","TRUNC","TZ_OFFSET","UID","UPPER","USER","USERENV","VAR_POP","VAR_SAMP","VARIANCE","VSIZE"
]

context = {
    "p_ext_list"    : ["ddl", "dml", "pkb", "pks", "seq", "sql", "tab", "tpb", "tps", "tst", "vw"],
    "p_uuid"        : "28DCE4DD-F5E1-4ED3-8847-64DA6B1F9163",
    "keyword_list"  : sorted(list(set(ORACLE_RESERVED_WORDS + ORACLE_KEYWORDS + ORACLE_PLSQL_RESERVED_WORDS))),
    "identifier"    : "[a-z0-9_\"#$]+",
    "type_list"     : sorted(list(set(ORACLE_TYPES))),
    "function_list" : sorted(list(set(ORACLE_BUILTIN_FUNCTIONS))),
}

class Dict(object):
    def __init__(self, **kwargs):
        self._items = kwargs
    def print(self, lines, level):
        lines.append("%s<dict>" % ("    " * level))
        for k in sorted(self._items.keys()):
            lines.append("%s<key>%s</key>" % ("    " * (level + 1), k))
            if isinstance(self._items[k], str):
                lines.append("%s<string>%s</string>" % ("    " * (level + 1), html.escape(self._items[k])))
            else:
                self._items[k].print(lines, level + 1)
        lines.append("%s</dict>" % ("    " * level))
    def update(self, **kwargs):
        for k, v in kwargs.items():
            if k in self._items:
                if isinstance(v, Dict):
                    self._items[k].update(**v._items)
                else:
                    assert False, "Unknown type";
            else:
                self._items.update({k : v})

class Array(object):
    def __init__(self, *args):
        self._items = [ i for i in args ]
    def print(self, lines, level):
        lines.append("%s<array>" % ("    " * level))
        for i in self._items:
            if isinstance(i, str):
                lines.append("%s<string>%s</string>" % ("    " * (level + 1), html.escape(i)))
            else:
                i.print(lines, level + 1)
        lines.append("%s</array>" % ("    " * level))

class Block(object):
    def __init__(self, name, begin, end):
        self._dict = Dict(name=name, begin=begin, end=end)
    def print(self, lines, level):
        self._dict.print(lines, level)

class Match(object):
    def __init__(self, name, match, captures=None):
        self._dict = Dict(name=name, match=match)
        if captures is not None:
            self._dict.update(captures=captures)
    def print(self, lines, level):
        self._dict.print(lines, level)

class Captures(object):
    def __init__(self, *args):
        d = {}
        for n, a in enumerate(args):
            d["%d" % (n + 1)] = a
        self._captures = Dict(**d)
    def print(self, lines, level):
        self._captures.print(lines, level)

from inspect import currentframe, getframeinfo
frameinfo = getframeinfo(currentframe())

#captures=Captures(Dict(nmae="asd"), Dict(nmae="asd"))

plist = Dict(
    name               = "PL/SQL (Oracle)",
    fileTypes          = Array("ddl", "dml", "pkb", "pks", "seq", "sql", "tab", "tpb", "tps", "tst", "vw"),
    foldingStartMarker = r"(?i)^\s*(xxx)\b",
    foldingStopMarker  = r"(?i)^\s*(yyy)\b",
    keyEquivalent      = "^~S",
    scopeName          = "source.plsql.oracle",
    uuid               = "28DCE4DD-F5E1-4ED3-8847-64DA6B1F9163",
    patterns           = Array(
        Block(name="comment.block.oracle",            begin=r"/\*", end=r"\*/"),
        Match(name="comment.line.oracle",             match=r"--.*$"),
        Block(name="string.oracle",                   begin=r"'",   end=r"'"),
        Block(name="string.quoted.oracle",            begin=r"q'!", end=r"!'"),
        Match(name="constant.boolean.oracle",         match=r"(?i)\b(true|false)\b"),
        Match(name="constant.numeric.oracle",         match=r"\b\d+(\.\d+)?\b"),
        #Match(name="keyword.control.oracle",          match=r"(?i)\b(if|elsif|else|end\s+if|loop|end\s+loop|for|case|end\s+case|continue|return|goto)\b"),
        #Match(name="keyword.operator.oracle",         match=r"(?i)\b(or|and|not|like|between)\b"),
        Match(name="keyword.operator.oracle",         match=r"[!<>:]?=|<>|<|>|\+|(?<!\.)\*|-|(?<!^)/|\|\||[();.,]"),
        #Match(name="keyword.other.oracle",            match=r"(?i)\b(merge|on|matched|returning|constant|with|using|execute\s+immediate|raise|pipe\s+row|bulk\s+collect|pipelined|parallel_enable|partition|by|any|declare|path|columns|passing|pragma|exception_init|autonomous_transaction|plsql_unit|plsql_line|forall|end|then|exception|when|others|begin|in|out|is|as|exit|open|fetch|into|close|type|subtype|record|rowtype|default|\.(extend|count|first|last|next|nextval|currval))\b"),
        #Match(name="keyword.other.sql.oracle",        match=r"(?i)\b(while|nocopy|force|authid|current_user|object|left|join|right|full|cross|select|from|where|order\s+by|group\s+by|asc|desc|update|set|insert|into|values|delete|from|distinct|union|having|limit|table|of)\b"),
        #Match(name="meta.create.oracle"   ,           match=r"(?i)^\s*(create)(\s+or\s+replace)?\s+"       , captures=Captures(Dict(name="keyword.other.oracle"), Dict(name="keyword.other.oracle"))),
        #Match(name="meta.package.oracle"  ,           match=r"(?i)\b(package)(\s+body)?\s+(\S+)"           , captures=Captures(Dict(name="keyword.other.oracle"), Dict(name="keyword.other.oracle"), Dict(name="entity.name.type.oracle"))),
        #Match(name="meta.procedure.oracle",           match=r'(?i)^\s*(function|procedure)\s+([-a-z0-9_]+)', captures=Captures(Dict(name="keyword.other.oracle"), Dict(name="entity.name.function.oracle"))),
        #Match(name="meta.procedure.oracle",           match=r'(?i)^\s*(member|static|constructor)\s+(function|procedure)\s+([-a-z0-9_]+)', captures=Captures(Dict(name="keyword.other.oracle"), Dict(name="entity.name.function.oracle"))),
        #Match(name="meta.type.oracle",                match=r'(?i)\b(type)\s+"([^"]+)"'                    , captures=Captures(Dict(name="keyword.other.oracle"), Dict(name="entity.name.type.oracle"))),
        #Match(name="support.class.oracle",            match=r"(?i)\b(dbms_lock|dbms_output|dbms_sql|dbms_xmldom|dbms_obfuscation_toolkit)\b"),
        #Match(name="support.function.builtin.oracle", match=r"(?i)\b(cursor|sys_context|over|xmltable|xmltype|replace|coalesce|exists|avg|count|sum|max|min|nvl|trim|to_date|to_char|lpad|ltrim|rpad|rtrim|trunc|to_number)\b"),
        #Match(name="support.function.oracle",         match=r"(?i)\b(put_line)\b"),
        #Match(name="support.function.oracle",         match=r"(?i)\b(systimestamp|sysdate|%(isopen|found|notfound|rowcount)|commit\s+write\s+nowait|commit|rollback|sqlerrm|substr|cast|decode|length|lower|upper|least|greatest|instr|chr)\b"),
        #Match(name="variable.language.oracle",        match=r"(?i)\b(sql|sqlcode)\b"),
        #Match(name="variable.other.oracle",           match=r"(?i)\b(l_[-a-z0-9_]+)\b"),
        #Match(name="variable.parameter.oracle",       match=r"(?i)\b(p(i|o|io)_[-a-z0-9_]+)\b"),
        Match(name="keyword.sql.oracle",              match=r"(?i)\b(CREATE|SELECT|UPDATE|DELETE|MERGE|ALTER|DROP)\b"),
        Match(name="type.oracle",                     match=r"(?i)\b(%s)\b" % "|".join( sorted(list(set(ORACLE_TYPES)))) ),
        Match(name="keyword.oracle",                  match=r"(?i)\b(%s)\b" % "|".join( sorted(list(set(ORACLE_RESERVED_WORDS + ORACLE_KEYWORDS + ORACLE_PLSQL_RESERVED_WORDS)))) ),
    )
)

settings = Dict(
    name     = "sotinov dark",
    author   = "Sergey Otinov",
    comment  = "Darck scheme for SublimeText",
    uuid     = "2C24E84F-F9FE-4C2E-92D2-F52198BA7E41",
    settings = Array(
        Dict(
            settings=Dict(
                background        = "#303030",
                caret             = "#FFFF00",
                foreground        = "#FFFFFF",
                inactiveSelection = "#606060FF",
                invisibles        = "#C0C0C0",
                lineHighlight     = "#404040",
                selection         = "#585858FF",
                selectionBorder   = "#808080",
            )
        ),
        Dict(name="String",         scope="string",           settings=Dict(foreground="#FF9900", background="#000000")),
        Dict(name="Entity/Keyword", scope="entity,keyword",   settings=Dict(foreground="#FFFF98")),
        Dict(name="Comment",        scope="comment",          settings=Dict(foreground="#808080")),
        Dict(name="Constant",       scope="constant.numeric", settings=Dict(foreground="#FF9900")),
        Dict(name="Type",           scope="type",             settings=Dict(foreground="#00FF00")),
        Dict(name="Op",             scope="keyword.operator", settings=Dict(foreground="#00FFFF")),
        Dict(name="Op",             scope="keyword.sql",      settings=Dict(foreground="#FFFF98", fontStyle="bold")),
    )
)

def main1():
    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append('<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">')
    lines.append('<plist version="1.0">')
    plist.print(lines, 0)
    lines.append('</plist>')
    s = "\n".join(lines)
    print(s)
    f = open("/home/sotinov/.config/sublime-text-2/Packages/Oracle PLSQL/PLSQL.tmLanguage", "w+")
    f.write(s)
    f.close()

    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append('<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">')
    lines.append('<plist version="1.0">')
    settings.print(lines, 0)
    lines.append('</plist>')
    s = "\n".join(lines)
    print(s)
    f = open("/home/sotinov/.config/sublime-text-2/Packages/Color Scheme - Default/sotinov_dark.tmTheme", "w+")
    f.write(s)
    f.close()

def main():
    env = jinja2.Environment(
        loader        = jinja2.FileSystemLoader("src/main/resources/templates"),
        trim_blocks   = True,
        lstrip_blocks = True,
        extensions    = ["jinja2.ext.do"]
    )
    templ = env.get_template("PLSQL.tmLanguage")
    out = templ.render(context)
    with open("PLSQL.tmLanguage", "w+") as f:
        f.write(out)

if __name__ == "__main__":
    main1()
