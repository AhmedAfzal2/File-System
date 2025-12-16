// Generated from c:/Stuff/University/Semester 4/Operating Systems/Labs/Lab 10, 11 OEL/File-System/FileSystem.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class FileSystemParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CREATE=1, DELETE_FILE=2, DELETE_DIR=3, MKDIR=4, CHDIR=5, MOVE_FILE=6, 
		MOVE_DIR=7, OPEN=8, CLOSE=9, WRITE_TO_FILE=10, READ_FROM_FILE=11, MOVE_WITHIN_FILE=12, 
		TRUNCATE_FILE=13, LS=14, SHOW_MEMORY_MAP=15, EXIT=16, INT=17, ID=18, STRING=19, 
		WS=20;
	public static final int
		RULE_root = 0, RULE_command = 1, RULE_create_cmd = 2, RULE_delete_file_cmd = 3, 
		RULE_delete_dir_cmd = 4, RULE_mkdir_cmd = 5, RULE_chdir_cmd = 6, RULE_move_file_cmd = 7, 
		RULE_move_dir_cmd = 8, RULE_open_cmd = 9, RULE_close_cmd = 10, RULE_write_to_file_cmd = 11, 
		RULE_read_from_file_cmd = 12, RULE_move_within_file_cmd = 13, RULE_truncate_file_cmd = 14, 
		RULE_ls_cmd = 15, RULE_show_memory_map_cmd = 16, RULE_exit_cmd = 17, RULE_path = 18, 
		RULE_open_mode = 19, RULE_data = 20;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "command", "create_cmd", "delete_file_cmd", "delete_dir_cmd", 
			"mkdir_cmd", "chdir_cmd", "move_file_cmd", "move_dir_cmd", "open_cmd", 
			"close_cmd", "write_to_file_cmd", "read_from_file_cmd", "move_within_file_cmd", 
			"truncate_file_cmd", "ls_cmd", "show_memory_map_cmd", "exit_cmd", "path", 
			"open_mode", "data"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CREATE", "DELETE_FILE", "DELETE_DIR", "MKDIR", "CHDIR", "MOVE_FILE", 
			"MOVE_DIR", "OPEN", "CLOSE", "WRITE_TO_FILE", "READ_FROM_FILE", "MOVE_WITHIN_FILE", 
			"TRUNCATE_FILE", "LS", "SHOW_MEMORY_MAP", "EXIT", "INT", "ID", "STRING", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "FileSystem.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public FileSystemParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public CommandContext command() {
			return getRuleContext(CommandContext.class,0);
		}
		public TerminalNode EOF() { return getToken(FileSystemParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			command();
			setState(43);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandContext extends ParserRuleContext {
		public Create_cmdContext create_cmd() {
			return getRuleContext(Create_cmdContext.class,0);
		}
		public Delete_file_cmdContext delete_file_cmd() {
			return getRuleContext(Delete_file_cmdContext.class,0);
		}
		public Delete_dir_cmdContext delete_dir_cmd() {
			return getRuleContext(Delete_dir_cmdContext.class,0);
		}
		public Mkdir_cmdContext mkdir_cmd() {
			return getRuleContext(Mkdir_cmdContext.class,0);
		}
		public Chdir_cmdContext chdir_cmd() {
			return getRuleContext(Chdir_cmdContext.class,0);
		}
		public Move_file_cmdContext move_file_cmd() {
			return getRuleContext(Move_file_cmdContext.class,0);
		}
		public Move_dir_cmdContext move_dir_cmd() {
			return getRuleContext(Move_dir_cmdContext.class,0);
		}
		public Open_cmdContext open_cmd() {
			return getRuleContext(Open_cmdContext.class,0);
		}
		public Close_cmdContext close_cmd() {
			return getRuleContext(Close_cmdContext.class,0);
		}
		public Write_to_file_cmdContext write_to_file_cmd() {
			return getRuleContext(Write_to_file_cmdContext.class,0);
		}
		public Read_from_file_cmdContext read_from_file_cmd() {
			return getRuleContext(Read_from_file_cmdContext.class,0);
		}
		public Move_within_file_cmdContext move_within_file_cmd() {
			return getRuleContext(Move_within_file_cmdContext.class,0);
		}
		public Truncate_file_cmdContext truncate_file_cmd() {
			return getRuleContext(Truncate_file_cmdContext.class,0);
		}
		public Ls_cmdContext ls_cmd() {
			return getRuleContext(Ls_cmdContext.class,0);
		}
		public Show_memory_map_cmdContext show_memory_map_cmd() {
			return getRuleContext(Show_memory_map_cmdContext.class,0);
		}
		public Exit_cmdContext exit_cmd() {
			return getRuleContext(Exit_cmdContext.class,0);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_command);
		try {
			setState(61);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CREATE:
				enterOuterAlt(_localctx, 1);
				{
				setState(45);
				create_cmd();
				}
				break;
			case DELETE_FILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(46);
				delete_file_cmd();
				}
				break;
			case DELETE_DIR:
				enterOuterAlt(_localctx, 3);
				{
				setState(47);
				delete_dir_cmd();
				}
				break;
			case MKDIR:
				enterOuterAlt(_localctx, 4);
				{
				setState(48);
				mkdir_cmd();
				}
				break;
			case CHDIR:
				enterOuterAlt(_localctx, 5);
				{
				setState(49);
				chdir_cmd();
				}
				break;
			case MOVE_FILE:
				enterOuterAlt(_localctx, 6);
				{
				setState(50);
				move_file_cmd();
				}
				break;
			case MOVE_DIR:
				enterOuterAlt(_localctx, 7);
				{
				setState(51);
				move_dir_cmd();
				}
				break;
			case OPEN:
				enterOuterAlt(_localctx, 8);
				{
				setState(52);
				open_cmd();
				}
				break;
			case CLOSE:
				enterOuterAlt(_localctx, 9);
				{
				setState(53);
				close_cmd();
				}
				break;
			case WRITE_TO_FILE:
				enterOuterAlt(_localctx, 10);
				{
				setState(54);
				write_to_file_cmd();
				}
				break;
			case READ_FROM_FILE:
				enterOuterAlt(_localctx, 11);
				{
				setState(55);
				read_from_file_cmd();
				}
				break;
			case MOVE_WITHIN_FILE:
				enterOuterAlt(_localctx, 12);
				{
				setState(56);
				move_within_file_cmd();
				}
				break;
			case TRUNCATE_FILE:
				enterOuterAlt(_localctx, 13);
				{
				setState(57);
				truncate_file_cmd();
				}
				break;
			case LS:
				enterOuterAlt(_localctx, 14);
				{
				setState(58);
				ls_cmd();
				}
				break;
			case SHOW_MEMORY_MAP:
				enterOuterAlt(_localctx, 15);
				{
				setState(59);
				show_memory_map_cmd();
				}
				break;
			case EXIT:
				enterOuterAlt(_localctx, 16);
				{
				setState(60);
				exit_cmd();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Create_cmdContext extends ParserRuleContext {
		public TerminalNode CREATE() { return getToken(FileSystemParser.CREATE, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public Create_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_create_cmd; }
	}

	public final Create_cmdContext create_cmd() throws RecognitionException {
		Create_cmdContext _localctx = new Create_cmdContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_create_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(CREATE);
			setState(64);
			path();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Delete_file_cmdContext extends ParserRuleContext {
		public TerminalNode DELETE_FILE() { return getToken(FileSystemParser.DELETE_FILE, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public Delete_file_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_delete_file_cmd; }
	}

	public final Delete_file_cmdContext delete_file_cmd() throws RecognitionException {
		Delete_file_cmdContext _localctx = new Delete_file_cmdContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_delete_file_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(DELETE_FILE);
			setState(67);
			path();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Delete_dir_cmdContext extends ParserRuleContext {
		public TerminalNode DELETE_DIR() { return getToken(FileSystemParser.DELETE_DIR, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public Delete_dir_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_delete_dir_cmd; }
	}

	public final Delete_dir_cmdContext delete_dir_cmd() throws RecognitionException {
		Delete_dir_cmdContext _localctx = new Delete_dir_cmdContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_delete_dir_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			match(DELETE_DIR);
			setState(70);
			path();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Mkdir_cmdContext extends ParserRuleContext {
		public TerminalNode MKDIR() { return getToken(FileSystemParser.MKDIR, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public Mkdir_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mkdir_cmd; }
	}

	public final Mkdir_cmdContext mkdir_cmd() throws RecognitionException {
		Mkdir_cmdContext _localctx = new Mkdir_cmdContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_mkdir_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(MKDIR);
			setState(73);
			path();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Chdir_cmdContext extends ParserRuleContext {
		public TerminalNode CHDIR() { return getToken(FileSystemParser.CHDIR, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public Chdir_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_chdir_cmd; }
	}

	public final Chdir_cmdContext chdir_cmd() throws RecognitionException {
		Chdir_cmdContext _localctx = new Chdir_cmdContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_chdir_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(CHDIR);
			setState(76);
			path();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Move_file_cmdContext extends ParserRuleContext {
		public PathContext src;
		public PathContext dest;
		public TerminalNode MOVE_FILE() { return getToken(FileSystemParser.MOVE_FILE, 0); }
		public List<PathContext> path() {
			return getRuleContexts(PathContext.class);
		}
		public PathContext path(int i) {
			return getRuleContext(PathContext.class,i);
		}
		public Move_file_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_move_file_cmd; }
	}

	public final Move_file_cmdContext move_file_cmd() throws RecognitionException {
		Move_file_cmdContext _localctx = new Move_file_cmdContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_move_file_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(MOVE_FILE);
			setState(79);
			((Move_file_cmdContext)_localctx).src = path();
			setState(80);
			((Move_file_cmdContext)_localctx).dest = path();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Move_dir_cmdContext extends ParserRuleContext {
		public PathContext src;
		public PathContext dest;
		public TerminalNode MOVE_DIR() { return getToken(FileSystemParser.MOVE_DIR, 0); }
		public List<PathContext> path() {
			return getRuleContexts(PathContext.class);
		}
		public PathContext path(int i) {
			return getRuleContext(PathContext.class,i);
		}
		public Move_dir_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_move_dir_cmd; }
	}

	public final Move_dir_cmdContext move_dir_cmd() throws RecognitionException {
		Move_dir_cmdContext _localctx = new Move_dir_cmdContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_move_dir_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(MOVE_DIR);
			setState(83);
			((Move_dir_cmdContext)_localctx).src = path();
			setState(84);
			((Move_dir_cmdContext)_localctx).dest = path();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Open_cmdContext extends ParserRuleContext {
		public TerminalNode OPEN() { return getToken(FileSystemParser.OPEN, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public Open_modeContext open_mode() {
			return getRuleContext(Open_modeContext.class,0);
		}
		public Open_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_open_cmd; }
	}

	public final Open_cmdContext open_cmd() throws RecognitionException {
		Open_cmdContext _localctx = new Open_cmdContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_open_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(OPEN);
			setState(87);
			path();
			setState(88);
			open_mode();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Close_cmdContext extends ParserRuleContext {
		public TerminalNode CLOSE() { return getToken(FileSystemParser.CLOSE, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public Close_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_close_cmd; }
	}

	public final Close_cmdContext close_cmd() throws RecognitionException {
		Close_cmdContext _localctx = new Close_cmdContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_close_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(CLOSE);
			setState(91);
			path();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Write_to_file_cmdContext extends ParserRuleContext {
		public Token offset;
		public TerminalNode WRITE_TO_FILE() { return getToken(FileSystemParser.WRITE_TO_FILE, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public DataContext data() {
			return getRuleContext(DataContext.class,0);
		}
		public TerminalNode INT() { return getToken(FileSystemParser.INT, 0); }
		public Write_to_file_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write_to_file_cmd; }
	}

	public final Write_to_file_cmdContext write_to_file_cmd() throws RecognitionException {
		Write_to_file_cmdContext _localctx = new Write_to_file_cmdContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_write_to_file_cmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(WRITE_TO_FILE);
			setState(94);
			path();
			setState(95);
			data();
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INT) {
				{
				setState(96);
				((Write_to_file_cmdContext)_localctx).offset = match(INT);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Read_from_file_cmdContext extends ParserRuleContext {
		public Token start;
		public Token size;
		public TerminalNode READ_FROM_FILE() { return getToken(FileSystemParser.READ_FROM_FILE, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public List<TerminalNode> INT() { return getTokens(FileSystemParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(FileSystemParser.INT, i);
		}
		public Read_from_file_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read_from_file_cmd; }
	}

	public final Read_from_file_cmdContext read_from_file_cmd() throws RecognitionException {
		Read_from_file_cmdContext _localctx = new Read_from_file_cmdContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_read_from_file_cmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(READ_FROM_FILE);
			setState(100);
			path();
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INT) {
				{
				setState(101);
				((Read_from_file_cmdContext)_localctx).start = match(INT);
				setState(102);
				((Read_from_file_cmdContext)_localctx).size = match(INT);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Move_within_file_cmdContext extends ParserRuleContext {
		public Token src;
		public Token dest;
		public Token size;
		public TerminalNode MOVE_WITHIN_FILE() { return getToken(FileSystemParser.MOVE_WITHIN_FILE, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public List<TerminalNode> INT() { return getTokens(FileSystemParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(FileSystemParser.INT, i);
		}
		public Move_within_file_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_move_within_file_cmd; }
	}

	public final Move_within_file_cmdContext move_within_file_cmd() throws RecognitionException {
		Move_within_file_cmdContext _localctx = new Move_within_file_cmdContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_move_within_file_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			match(MOVE_WITHIN_FILE);
			setState(106);
			path();
			setState(107);
			((Move_within_file_cmdContext)_localctx).src = match(INT);
			setState(108);
			((Move_within_file_cmdContext)_localctx).dest = match(INT);
			setState(109);
			((Move_within_file_cmdContext)_localctx).size = match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Truncate_file_cmdContext extends ParserRuleContext {
		public Token size;
		public TerminalNode TRUNCATE_FILE() { return getToken(FileSystemParser.TRUNCATE_FILE, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public TerminalNode INT() { return getToken(FileSystemParser.INT, 0); }
		public Truncate_file_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_truncate_file_cmd; }
	}

	public final Truncate_file_cmdContext truncate_file_cmd() throws RecognitionException {
		Truncate_file_cmdContext _localctx = new Truncate_file_cmdContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_truncate_file_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(TRUNCATE_FILE);
			setState(112);
			path();
			setState(113);
			((Truncate_file_cmdContext)_localctx).size = match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Ls_cmdContext extends ParserRuleContext {
		public TerminalNode LS() { return getToken(FileSystemParser.LS, 0); }
		public Ls_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ls_cmd; }
	}

	public final Ls_cmdContext ls_cmd() throws RecognitionException {
		Ls_cmdContext _localctx = new Ls_cmdContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_ls_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(LS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Show_memory_map_cmdContext extends ParserRuleContext {
		public TerminalNode SHOW_MEMORY_MAP() { return getToken(FileSystemParser.SHOW_MEMORY_MAP, 0); }
		public Show_memory_map_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_show_memory_map_cmd; }
	}

	public final Show_memory_map_cmdContext show_memory_map_cmd() throws RecognitionException {
		Show_memory_map_cmdContext _localctx = new Show_memory_map_cmdContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_show_memory_map_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(SHOW_MEMORY_MAP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Exit_cmdContext extends ParserRuleContext {
		public TerminalNode EXIT() { return getToken(FileSystemParser.EXIT, 0); }
		public Exit_cmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exit_cmd; }
	}

	public final Exit_cmdContext exit_cmd() throws RecognitionException {
		Exit_cmdContext _localctx = new Exit_cmdContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_exit_cmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(EXIT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PathContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(FileSystemParser.STRING, 0); }
		public TerminalNode ID() { return getToken(FileSystemParser.ID, 0); }
		public PathContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_path; }
	}

	public final PathContext path() throws RecognitionException {
		PathContext _localctx = new PathContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_path);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==STRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Open_modeContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(FileSystemParser.STRING, 0); }
		public TerminalNode ID() { return getToken(FileSystemParser.ID, 0); }
		public Open_modeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_open_mode; }
	}

	public final Open_modeContext open_mode() throws RecognitionException {
		Open_modeContext _localctx = new Open_modeContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_open_mode);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==STRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DataContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(FileSystemParser.STRING, 0); }
		public TerminalNode ID() { return getToken(FileSystemParser.ID, 0); }
		public DataContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_data; }
	}

	public final DataContext data() throws RecognitionException {
		DataContext _localctx = new DataContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_data);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==STRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0014\u0080\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003"+
		"\u0001>\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0003\u000bb\b\u000b\u0001\f\u0001\f\u0001\f"+
		"\u0001\f\u0003\fh\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0000\u0000"+
		"\u0015\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u001c\u001e \"$&(\u0000\u0001\u0001\u0000\u0012\u0013{\u0000*\u0001"+
		"\u0000\u0000\u0000\u0002=\u0001\u0000\u0000\u0000\u0004?\u0001\u0000\u0000"+
		"\u0000\u0006B\u0001\u0000\u0000\u0000\bE\u0001\u0000\u0000\u0000\nH\u0001"+
		"\u0000\u0000\u0000\fK\u0001\u0000\u0000\u0000\u000eN\u0001\u0000\u0000"+
		"\u0000\u0010R\u0001\u0000\u0000\u0000\u0012V\u0001\u0000\u0000\u0000\u0014"+
		"Z\u0001\u0000\u0000\u0000\u0016]\u0001\u0000\u0000\u0000\u0018c\u0001"+
		"\u0000\u0000\u0000\u001ai\u0001\u0000\u0000\u0000\u001co\u0001\u0000\u0000"+
		"\u0000\u001es\u0001\u0000\u0000\u0000 u\u0001\u0000\u0000\u0000\"w\u0001"+
		"\u0000\u0000\u0000$y\u0001\u0000\u0000\u0000&{\u0001\u0000\u0000\u0000"+
		"(}\u0001\u0000\u0000\u0000*+\u0003\u0002\u0001\u0000+,\u0005\u0000\u0000"+
		"\u0001,\u0001\u0001\u0000\u0000\u0000->\u0003\u0004\u0002\u0000.>\u0003"+
		"\u0006\u0003\u0000/>\u0003\b\u0004\u00000>\u0003\n\u0005\u00001>\u0003"+
		"\f\u0006\u00002>\u0003\u000e\u0007\u00003>\u0003\u0010\b\u00004>\u0003"+
		"\u0012\t\u00005>\u0003\u0014\n\u00006>\u0003\u0016\u000b\u00007>\u0003"+
		"\u0018\f\u00008>\u0003\u001a\r\u00009>\u0003\u001c\u000e\u0000:>\u0003"+
		"\u001e\u000f\u0000;>\u0003 \u0010\u0000<>\u0003\"\u0011\u0000=-\u0001"+
		"\u0000\u0000\u0000=.\u0001\u0000\u0000\u0000=/\u0001\u0000\u0000\u0000"+
		"=0\u0001\u0000\u0000\u0000=1\u0001\u0000\u0000\u0000=2\u0001\u0000\u0000"+
		"\u0000=3\u0001\u0000\u0000\u0000=4\u0001\u0000\u0000\u0000=5\u0001\u0000"+
		"\u0000\u0000=6\u0001\u0000\u0000\u0000=7\u0001\u0000\u0000\u0000=8\u0001"+
		"\u0000\u0000\u0000=9\u0001\u0000\u0000\u0000=:\u0001\u0000\u0000\u0000"+
		"=;\u0001\u0000\u0000\u0000=<\u0001\u0000\u0000\u0000>\u0003\u0001\u0000"+
		"\u0000\u0000?@\u0005\u0001\u0000\u0000@A\u0003$\u0012\u0000A\u0005\u0001"+
		"\u0000\u0000\u0000BC\u0005\u0002\u0000\u0000CD\u0003$\u0012\u0000D\u0007"+
		"\u0001\u0000\u0000\u0000EF\u0005\u0003\u0000\u0000FG\u0003$\u0012\u0000"+
		"G\t\u0001\u0000\u0000\u0000HI\u0005\u0004\u0000\u0000IJ\u0003$\u0012\u0000"+
		"J\u000b\u0001\u0000\u0000\u0000KL\u0005\u0005\u0000\u0000LM\u0003$\u0012"+
		"\u0000M\r\u0001\u0000\u0000\u0000NO\u0005\u0006\u0000\u0000OP\u0003$\u0012"+
		"\u0000PQ\u0003$\u0012\u0000Q\u000f\u0001\u0000\u0000\u0000RS\u0005\u0007"+
		"\u0000\u0000ST\u0003$\u0012\u0000TU\u0003$\u0012\u0000U\u0011\u0001\u0000"+
		"\u0000\u0000VW\u0005\b\u0000\u0000WX\u0003$\u0012\u0000XY\u0003&\u0013"+
		"\u0000Y\u0013\u0001\u0000\u0000\u0000Z[\u0005\t\u0000\u0000[\\\u0003$"+
		"\u0012\u0000\\\u0015\u0001\u0000\u0000\u0000]^\u0005\n\u0000\u0000^_\u0003"+
		"$\u0012\u0000_a\u0003(\u0014\u0000`b\u0005\u0011\u0000\u0000a`\u0001\u0000"+
		"\u0000\u0000ab\u0001\u0000\u0000\u0000b\u0017\u0001\u0000\u0000\u0000"+
		"cd\u0005\u000b\u0000\u0000dg\u0003$\u0012\u0000ef\u0005\u0011\u0000\u0000"+
		"fh\u0005\u0011\u0000\u0000ge\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000"+
		"\u0000h\u0019\u0001\u0000\u0000\u0000ij\u0005\f\u0000\u0000jk\u0003$\u0012"+
		"\u0000kl\u0005\u0011\u0000\u0000lm\u0005\u0011\u0000\u0000mn\u0005\u0011"+
		"\u0000\u0000n\u001b\u0001\u0000\u0000\u0000op\u0005\r\u0000\u0000pq\u0003"+
		"$\u0012\u0000qr\u0005\u0011\u0000\u0000r\u001d\u0001\u0000\u0000\u0000"+
		"st\u0005\u000e\u0000\u0000t\u001f\u0001\u0000\u0000\u0000uv\u0005\u000f"+
		"\u0000\u0000v!\u0001\u0000\u0000\u0000wx\u0005\u0010\u0000\u0000x#\u0001"+
		"\u0000\u0000\u0000yz\u0007\u0000\u0000\u0000z%\u0001\u0000\u0000\u0000"+
		"{|\u0007\u0000\u0000\u0000|\'\u0001\u0000\u0000\u0000}~\u0007\u0000\u0000"+
		"\u0000~)\u0001\u0000\u0000\u0000\u0003=ag";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}