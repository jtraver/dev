# https://golang.org/pkg/

# The Go Programming Language
# Documents Packages The Project Help Blog Play  
# Packages

# Standard library
# Other packages
# Sub-repositories
# Community
# Standard library 
# Name    Synopsis
echo
echo "---------------------------------------------------------------------------------"
echo go doc archive 
# go doc archive 

echo
echo "---------------------------------------------------------------------------------"
echo go doc tar # # Package tar implements access to tar archives.
go doc tar # # Package tar implements access to tar archives.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
go doc zip # # Package zip provides support for reading and writing ZIP archives.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
go doc bufio   # # Package bufio implements buffered I/O. It wraps an io.Reader or io.Writer object, creating another object (Reader or Writer) that also implements the interface but provides buffering and some help for textual I/O.
echo
echo "---------------------------------------------------------------------------------"
go doc builtin # # Package builtin provides documentation for Go's predeclared identifiers.
echo
echo "---------------------------------------------------------------------------------"
go doc bytes   # # Package bytes implements functions for the manipulation of byte slices.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
echo go doc compress    
# go doc compress    

echo
echo "---------------------------------------------------------------------------------"
go doc bzip2   # # Package bzip2 implements bzip2 decompression.
echo
echo "---------------------------------------------------------------------------------"
go doc flate   # # Package flate implements the DEFLATE compressed data format, described in RFC 1951.
echo
echo "---------------------------------------------------------------------------------"
go doc gzip    # # Package gzip implements reading and writing of gzip format compressed files, as specified in RFC 1952.
echo
echo "---------------------------------------------------------------------------------"
go doc lzw # # Package lzw implements the Lempel-Ziv-Welch compressed data format, described in T. A. Welch, ``A Technique for High-Performance Data Compression'', Computer, 17(6) (June 1984), pp 8-19.
echo
echo "---------------------------------------------------------------------------------"
go doc zlib    # # Package zlib implements reading and writing of zlib format compressed data, as specified in RFC 1950.
echo
echo
echo "---------------------------------------------------------------------------------"
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
echo go doc container   
# go doc container   

echo
echo "---------------------------------------------------------------------------------"
go doc heap    # # Package heap provides heap operations for any type that implements heap.Interface.
echo
echo "---------------------------------------------------------------------------------"
go doc list    # # Package list implements a doubly linked list.
echo
echo "---------------------------------------------------------------------------------"
go doc ring    # # Package ring implements operations on circular lists.
echo
echo "---------------------------------------------------------------------------------"
go doc context # # Package context defines the Context type, which carries deadlines, cancelation signals, and other request-scoped values across API boundaries and between processes.
echo
echo "---------------------------------------------------------------------------------"
go doc crypto  # # Package crypto collects common cryptographic constants.
echo
echo "---------------------------------------------------------------------------------"
go doc aes # Package aes implements AES encryption (formerly Rijndael), as defined in U.S. Federal Information Processing Standards Publication 197.
echo
echo "---------------------------------------------------------------------------------"
go doc cipher  # Package cipher implements standard block cipher modes that can be wrapped around low-level block cipher implementations.
echo
echo "---------------------------------------------------------------------------------"
go doc des # Package des implements the Data Encryption Standard (DES) and the Triple Data Encryption Algorithm (TDEA) as defined in U.S. Federal Information Processing Standards Publication 46-3.
echo
echo "---------------------------------------------------------------------------------"
go doc dsa # Package dsa implements the Digital Signature Algorithm, as defined in FIPS 186-3.
echo
echo "---------------------------------------------------------------------------------"
go doc ecdsa   # Package ecdsa implements the Elliptic Curve Digital Signature Algorithm, as defined in FIPS 186-3.
echo
echo "---------------------------------------------------------------------------------"
go doc elliptic    # Package elliptic implements several standard elliptic curves over prime fields.
echo
echo "---------------------------------------------------------------------------------"
go doc hmac    # Package hmac implements the Keyed-Hash Message Authentication Code (HMAC) as defined in U.S. Federal Information Processing Standards Publication 198.
echo
echo "---------------------------------------------------------------------------------"
go doc md5 # Package md5 implements the MD5 hash algorithm as defined in RFC 1321.
echo
echo "---------------------------------------------------------------------------------"
go doc rand    # Package rand implements a cryptographically secure pseudorandom number generator.
echo
echo "---------------------------------------------------------------------------------"
go doc rc4 # Package rc4 implements RC4 encryption, as defined in Bruce Schneier's Applied Cryptography.
echo
echo "---------------------------------------------------------------------------------"
go doc rsa # Package rsa implements RSA encryption as specified in PKCS#1.
echo
echo "---------------------------------------------------------------------------------"
go doc sha1    # Package sha1 implements the SHA1 hash algorithm as defined in RFC 3174.
echo
echo "---------------------------------------------------------------------------------"
go doc sha256  # Package sha256 implements the SHA224 and SHA256 hash algorithms as defined in FIPS 180-4.
echo
echo "---------------------------------------------------------------------------------"
go doc sha512  # Package sha512 implements the SHA-384, SHA-512, SHA-512/224, and SHA-512/256 hash algorithms as defined in FIPS 180-4.
echo
echo "---------------------------------------------------------------------------------"
go doc subtle  # Package subtle implements functions that are often useful in cryptographic code but require careful thought to use correctly.
echo
echo "---------------------------------------------------------------------------------"
go doc tls # Package tls partially implements TLS 1.2, as specified in RFC 5246.
echo
echo "---------------------------------------------------------------------------------"
go doc x509    # Package x509 parses X.509-encoded keys and certificates.
echo
echo "---------------------------------------------------------------------------------"
go doc pkix    # Package pkix contains shared, low level structures used for ASN.1 parsing and serialization of X.509 certificates, CRL and OCSP.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
echo go doc database    
# go doc database    

echo
echo "---------------------------------------------------------------------------------"
go doc sql # Package sql provides a generic interface around SQL (or SQL-like) databases.
echo
echo "---------------------------------------------------------------------------------"
go doc driver  # Package driver defines interfaces to be implemented by database drivers as used by package sql.
echo
echo "---------------------------------------------------------------------------------"
go doc debug   
echo
echo "---------------------------------------------------------------------------------"
go doc dwarf   # Package dwarf provides access to DWARF debugging information loaded from executable files, as defined in the DWARF 2.0 Standard at http://dwarfstd.org/doc/dwarf-2.0.0.pdf
echo
echo "---------------------------------------------------------------------------------"
go doc elf # Package elf implements access to ELF object files.
echo
echo "---------------------------------------------------------------------------------"
go doc gosym   # Package gosym implements access to the Go symbol and line number tables embedded in Go binaries generated by the gc compilers.
echo
echo "---------------------------------------------------------------------------------"
go doc macho   # Package macho implements access to Mach-O object files.
echo
echo "---------------------------------------------------------------------------------"
go doc pe  # Package pe implements access to PE (Microsoft Windows Portable Executable) files.
echo
echo "---------------------------------------------------------------------------------"
go doc plan9obj    # Package plan9obj implements access to Plan 9 a.out object files.
echo
echo "---------------------------------------------------------------------------------"
go doc encoding    # Package encoding defines interfaces shared by other packages that convert data to and from byte-level and textual representations.
echo
echo "---------------------------------------------------------------------------------"
go doc ascii85 # Package ascii85 implements the ascii85 data encoding as used in the btoa tool and Adobe's PostScript and PDF document formats.
echo
echo "---------------------------------------------------------------------------------"
go doc asn1    # Package asn1 implements parsing of DER-encoded ASN.1 data structures, as defined in ITU-T Rec X.690.
echo
echo "---------------------------------------------------------------------------------"
go doc base32  # Package base32 implements base32 encoding as specified by RFC 4648.
echo
echo "---------------------------------------------------------------------------------"
go doc base64  # Package base64 implements base64 encoding as specified by RFC 4648.
echo
echo "---------------------------------------------------------------------------------"
go doc binary  # Package binary implements simple translation between numbers and byte sequences and encoding and decoding of varints.
echo
echo "---------------------------------------------------------------------------------"
go doc csv # Package csv reads and writes comma-separated values (CSV) files.
echo
echo "---------------------------------------------------------------------------------"
go doc gob # Package gob manages streams of gobs - binary values exchanged between an Encoder (transmitter) and a Decoder (receiver).
echo
echo "---------------------------------------------------------------------------------"
go doc hex # Package hex implements hexadecimal encoding and decoding.
echo
echo "---------------------------------------------------------------------------------"
go doc json    # Package json implements encoding and decoding of JSON as defined in RFC 4627.
echo
echo "---------------------------------------------------------------------------------"
go doc pem # Package pem implements the PEM data encoding, which originated in Privacy Enhanced Mail.
echo
echo "---------------------------------------------------------------------------------"
go doc xml # Package xml implements a simple XML 1.0 parser that understands XML name spaces.
echo
echo "---------------------------------------------------------------------------------"
go doc errors  # Package errors implements functions to manipulate errors.
echo
echo "---------------------------------------------------------------------------------"
go doc expvar  # Package expvar provides a standardized interface to public variables, such as operation counters in servers.
echo
echo "---------------------------------------------------------------------------------"
go doc flag    # Package flag implements command-line flag parsing.
echo
echo "---------------------------------------------------------------------------------"
go doc fmt # Package fmt implements formatted I/O with functions analogous to C's printf and scanf.
echo
echo "---------------------------------------------------------------------------------"
echo go doc go  
go doc go  
echo
echo "---------------------------------------------------------------------------------"
go doc ast # Package ast declares the types used to represent syntax trees for Go packages.
echo
echo "---------------------------------------------------------------------------------"
go doc build   # Package build gathers information about Go packages.
echo
echo "---------------------------------------------------------------------------------"
go doc constant    # Package constant implements Values representing untyped Go constants and their corresponding operations.
echo
echo "---------------------------------------------------------------------------------"
go doc doc # Package doc extracts source code documentation from a Go AST.
echo
echo "---------------------------------------------------------------------------------"
go doc format  # Package format implements standard formatting of Go source.
echo
echo "---------------------------------------------------------------------------------"
go doc importer    # Package importer provides access to export data importers.
echo
echo "---------------------------------------------------------------------------------"
go doc parser  # Package parser implements a parser for Go source files.
echo
echo "---------------------------------------------------------------------------------"
go doc printer # Package printer implements printing of AST nodes.
echo
echo "---------------------------------------------------------------------------------"
go doc scanner # Package scanner implements a scanner for Go source text.
echo
echo "---------------------------------------------------------------------------------"
go doc token   # Package token defines constants representing the lexical tokens of the Go programming language and basic operations on tokens (printing, predicates).
echo
echo "---------------------------------------------------------------------------------"
go doc types   # Package types declares the data types and implements the algorithms for type-checking of Go packages.
echo
echo "---------------------------------------------------------------------------------"
go doc hash    # Package hash provides interfaces for hash functions.
echo
echo "---------------------------------------------------------------------------------"
go doc adler32 # Package adler32 implements the Adler-32 checksum.
echo
echo "---------------------------------------------------------------------------------"
go doc crc32   # Package crc32 implements the 32-bit cyclic redundancy check, or CRC-32, checksum.
echo
echo "---------------------------------------------------------------------------------"
go doc crc64   # Package crc64 implements the 64-bit cyclic redundancy check, or CRC-64, checksum.
echo
echo "---------------------------------------------------------------------------------"
go doc fnv # Package fnv implements FNV-1 and FNV-1a, non-cryptographic hash functions created by Glenn Fowler, Landon Curt Noll, and Phong Vo.
echo
echo "---------------------------------------------------------------------------------"
go doc html    # Package html provides functions for escaping and unescaping HTML text.
echo
echo "---------------------------------------------------------------------------------"
go doc template    # Package template (html/template) implements data-driven templates for generating HTML output safe against code injection.
echo
echo "---------------------------------------------------------------------------------"
go doc image   # Package image implements a basic 2-D image library.
echo
echo "---------------------------------------------------------------------------------"
go doc color   # Package color implements a basic color library.
echo
echo "---------------------------------------------------------------------------------"
go doc palette # Package palette provides standard color palettes.
echo
echo "---------------------------------------------------------------------------------"
go doc draw    # Package draw provides image composition functions.
echo
echo "---------------------------------------------------------------------------------"
go doc gif # Package gif implements a GIF image decoder and encoder.
echo
echo "---------------------------------------------------------------------------------"
go doc jpeg    # Package jpeg implements a JPEG image decoder and encoder.
echo
echo "---------------------------------------------------------------------------------"
go doc png # Package png implements a PNG image decoder and encoder.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
echo go doc index   
# go doc index   

echo
echo "---------------------------------------------------------------------------------"
go doc suffixarray # Package suffixarray implements substring search in logarithmic time using an in-memory suffix array.
echo
echo "---------------------------------------------------------------------------------"
go doc io  # Package io provides basic interfaces to I/O primitives.
echo
echo "---------------------------------------------------------------------------------"
go doc ioutil  # Package ioutil implements some I/O utility functions.
echo
echo "---------------------------------------------------------------------------------"
go doc log # Package log implements a simple logging package.
echo
echo "---------------------------------------------------------------------------------"
go doc syslog  # Package syslog provides a simple interface to the system log service.
echo
echo "---------------------------------------------------------------------------------"
go doc math    # Package math provides basic constants and mathematical functions.
echo
echo "---------------------------------------------------------------------------------"
go doc big # Package big implements arbitrary-precision arithmetic (big numbers).
echo
echo "---------------------------------------------------------------------------------"
go doc cmplx   # Package cmplx provides basic constants and mathematical functions for complex numbers.
echo
echo "---------------------------------------------------------------------------------"
go doc rand    # Package rand implements pseudo-random number generators.
echo
echo "---------------------------------------------------------------------------------"
go doc mime    # Package mime implements parts of the MIME spec.
echo
echo "---------------------------------------------------------------------------------"
go doc multipart   # Package multipart implements MIME multipart parsing, as defined in RFC 2046.
echo
echo "---------------------------------------------------------------------------------"
go doc quotedprintable # Package quotedprintable implements quoted-printable encoding as specified by RFC 2045.
echo
echo "---------------------------------------------------------------------------------"
go doc net # Package net provides a portable interface for network I/O, including TCP/IP, UDP, domain name resolution, and Unix domain sockets.
echo
echo "---------------------------------------------------------------------------------"
go doc http    # Package http provides HTTP client and server implementations.
echo
echo "---------------------------------------------------------------------------------"
go doc cgi # Package cgi implements CGI (Common Gateway Interface) as specified in RFC 3875.
echo
echo "---------------------------------------------------------------------------------"
go doc cookiejar   # Package cookiejar implements an in-memory RFC 6265-compliant http.CookieJar.
echo
echo "---------------------------------------------------------------------------------"
go doc fcgi    # Package fcgi implements the FastCGI protocol.
echo
echo "---------------------------------------------------------------------------------"
go doc httptest    # Package httptest provides utilities for HTTP testing.
echo
echo "---------------------------------------------------------------------------------"
go doc httptrace   # Package httptrace provides mechanisms to trace the events within HTTP client requests.
echo
echo "---------------------------------------------------------------------------------"
go doc httputil    # Package httputil provides HTTP utility functions, complementing the more common ones in the net/http package.
echo
echo "---------------------------------------------------------------------------------"
go doc pprof   # Package pprof serves via its HTTP server runtime profiling data in the format expected by the pprof visualization tool.
echo
echo "---------------------------------------------------------------------------------"
go doc mail    # Package mail implements parsing of mail messages.
echo
echo "---------------------------------------------------------------------------------"
go doc rpc # Package rpc provides access to the exported methods of an object across a network or other I/O connection.
echo
echo "---------------------------------------------------------------------------------"
go doc jsonrpc # Package jsonrpc implements a JSON-RPC ClientCodec and ServerCodec for the rpc package.
echo
echo "---------------------------------------------------------------------------------"
go doc smtp    # Package smtp implements the Simple Mail Transfer Protocol as defined in RFC 5321.
echo
echo "---------------------------------------------------------------------------------"
go doc textproto   # Package textproto implements generic support for text-based request/response protocols in the style of HTTP, NNTP, and SMTP.
echo
echo "---------------------------------------------------------------------------------"
go doc url # Package url parses URLs and implements query escaping.
echo
echo "---------------------------------------------------------------------------------"
go doc os  # Package os provides a platform-independent interface to operating system functionality.
echo
echo "---------------------------------------------------------------------------------"
go doc exec    # Package exec runs external commands.
echo
echo "---------------------------------------------------------------------------------"
go doc signal  # Package signal implements access to incoming signals.
echo
echo "---------------------------------------------------------------------------------"
go doc user    # Package user allows user account lookups by name or id.
echo
echo "---------------------------------------------------------------------------------"
go doc path    # Package path implements utility routines for manipulating slash-separated paths.
echo
echo "---------------------------------------------------------------------------------"
go doc filepath    # Package filepath implements utility routines for manipulating filename paths in a way compatible with the target operating system-defined file paths.
echo
echo "---------------------------------------------------------------------------------"
go doc reflect # Package reflect implements run-time reflection, allowing a program to manipulate objects with arbitrary types.
echo
echo "---------------------------------------------------------------------------------"
go doc regexp  # Package regexp implements regular expression search.
echo
echo "---------------------------------------------------------------------------------"
go doc syntax  # Package syntax parses regular expressions into parse trees and compiles parse trees into programs.
echo
echo "---------------------------------------------------------------------------------"
go doc runtime # Package runtime contains operations that interact with Go's runtime system, such as functions to control goroutines.
echo
echo "---------------------------------------------------------------------------------"
go doc cgo # Package cgo contains runtime support for code generated by the cgo tool.
echo
echo "---------------------------------------------------------------------------------"
go doc debug   # Package debug contains facilities for programs to debug themselves while they are running.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
echo go doc msan    
# go doc msan    

echo
echo "---------------------------------------------------------------------------------"
go doc pprof   # Package pprof writes runtime profiling data in the format expected by the pprof visualization tool.
echo
echo "---------------------------------------------------------------------------------"
go doc race    # Package race implements data race detection logic.
echo
echo "---------------------------------------------------------------------------------"
go doc trace   # Go execution tracer.
echo
echo "---------------------------------------------------------------------------------"
go doc sort    # Package sort provides primitives for sorting slices and user-defined collections.
echo
echo "---------------------------------------------------------------------------------"
go doc strconv # Package strconv implements conversions to and from string representations of basic data types.
echo
echo "---------------------------------------------------------------------------------"
go doc strings # Package strings implements simple functions to manipulate UTF-8 encoded strings.
echo
echo "---------------------------------------------------------------------------------"
go doc sync    # Package sync provides basic synchronization primitives such as mutual exclusion locks.
echo
echo "---------------------------------------------------------------------------------"
go doc atomic  # Package atomic provides low-level atomic memory primitives useful for implementing synchronization algorithms.
echo
echo "---------------------------------------------------------------------------------"
go doc syscall # Package syscall contains an interface to the low-level operating system primitives.
echo
echo "---------------------------------------------------------------------------------"
go doc testing # Package testing provides support for automated testing of Go packages.
echo
echo "---------------------------------------------------------------------------------"
go doc iotest  # Package iotest implements Readers and Writers useful mainly for testing.
echo
echo "---------------------------------------------------------------------------------"
go doc quick   # Package quick implements utility functions to help with black box testing.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
echo go doc text    
# go doc text    

echo
echo "---------------------------------------------------------------------------------"
go doc scanner # Package scanner provides a scanner and tokenizer for UTF-8-encoded text.
echo
echo "---------------------------------------------------------------------------------"
go doc tabwriter   # Package tabwriter implements a write filter (tabwriter.Writer) that translates tabbed columns in input into properly aligned text.
echo
echo "---------------------------------------------------------------------------------"
go doc template    # Package template implements data-driven templates for generating textual output.
echo
echo "---------------------------------------------------------------------------------"
go doc parse   # Package parse builds parse trees for templates as defined by text/template and html/template.
echo
echo "---------------------------------------------------------------------------------"
go doc time    # Package time provides functionality for measuring and displaying time.
echo
echo "---------------------------------------------------------------------------------"
go doc unicode # Package unicode provides data and functions to test some properties of Unicode code points.
echo
echo "---------------------------------------------------------------------------------"
go doc utf16   # Package utf16 implements encoding and decoding of UTF-16 sequences.
echo
echo "---------------------------------------------------------------------------------"
go doc utf8    # Package utf8 implements functions and constants to support text encoded in UTF-8.
echo
echo "---------------------------------------------------------------------------------"
go doc unsafe  # Package unsafe contains operations that step around the type safety of Go programs.
echo
echo "---------------------------------------------------------------------------------"

# Other packages
# Sub-repositories
# These packages are part of the Go Project but outside the main Go tree. They are developed under looser compatibility requirements than the Go core. Install them with "go get".
echo
echo "---------------------------------------------------------------------------------"
echo go doc benchmarks # — benchmarks to measure Go as it is developed.
# go doc benchmarks # — benchmarks to measure Go as it is developed.

echo
echo "---------------------------------------------------------------------------------"
echo go doc blog # — blog.golang.org's implementation.
# go doc blog # — blog.golang.org's implementation.

echo
echo "---------------------------------------------------------------------------------"
echo go doc build # — build.golang.org's implementation.
go doc build # — build.golang.org's implementation.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
echo go doc crypto # — additional cryptography packages.
go doc crypto # — additional cryptography packages.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
echo go doc debug # — an experimental debugger for Go.
go doc debug # — an experimental debugger for Go.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
echo go doc image # — additional imaging packages.
go doc image # — additional imaging packages.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
echo go doc mobile # — experimental support for Go on mobile platforms.
# go doc mobile # — experimental support for Go on mobile platforms.

echo
echo "---------------------------------------------------------------------------------"
echo go doc net # — additional networking packages.
go doc net # — additional networking packages.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
echo go doc sys # — packages for making system calls.
go doc sys # — packages for making system calls.
echo
echo "---------------------------------------------------------------------------------"
echo
echo "---------------------------------------------------------------------------------"
echo go doc text # — packages for working with text.
# go doc text # — packages for working with text.

echo
echo "---------------------------------------------------------------------------------"
echo go doc tools # — godoc, goimports, gorename, and other tools.
# go doc tools # — godoc, goimports, gorename, and other tools.

echo
echo "---------------------------------------------------------------------------------"
echo go doc tour # — tour.golang.org's implementation.
# go doc tour # — tour.golang.org's implementation.

echo
echo "---------------------------------------------------------------------------------"
echo go doc exp # — experimental and deprecated packages (handle with care; may change without warning).
# go doc exp # — experimental and deprecated packages (handle with care; may change without warning).

# Community
# These services can help you find Open Source packages provided by the community.

# GoDoc - a package index and search engine.
# Go Search - a code search engine.
# Projects at the Go Wiki - a curated list of Go projects.
# Build version go1.7.4.
# Except as noted, the content of this page is licensed under the Creative Commons Attribution 3.0 License, and code is licensed under a BSD license.
# Terms of Service | Privacy Policy
