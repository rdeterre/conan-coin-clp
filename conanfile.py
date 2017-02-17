from conans import ConanFile, ConfigureEnvironment

class ConanCointClp(ConanFile):
    name = "coin-clp"
    version = "1.16"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://projects.coin-or.org/Clp"
    license = "Eclipse Public License"
    generators = "cmake"

    def source(self):
        self.run("svn co --non-interactive --trust-server-cert https://projects.coin-or.org/svn/Clp/stable/1.16 coin-clp")

    def build(self):
        env = ConfigureEnvironment(self)
        self.run("cd coin-clp && {} ./configure".format(env.command_line_env))
        self.run("cd coin-clp && {} make".format(env.command_line_env))
        self.run("cd coin-clp && {} make".format(env.command_line_env))
        self.run("cd coin-clp && make install DESTDIR=`pwd`/tmp")

    def package(self):
        self.copy("*.hpp", dst="include/coin", src="coin-clp/tmp", keep_path=False)
        self.copy("*.h",   dst="include/coin", src="coin-clp/tmp", keep_path=False)
        self.copy("*.so*", dst="lib", src="coin-clp/tmp", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Osi", "Clp", "ClpSolver", "CoinUtils"]
        self.cpp_info.includedirs = ["include/coin"]
