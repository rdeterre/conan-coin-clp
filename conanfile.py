from conans import ConanFile, ConfigureEnvironment

class ConanCointClp(ConanFile):
    name = "coin-clp"
    version = "1.16"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://projects.coin-or.org/Clp"
    license = "Eclipse Public License"
    generators = "cmake"

    def source(self):
        self.run("svn co --trust-server-cert https://projects.coin-or.org/svn/Clp/stable/1.16 coin-clp")

    def build(self):
        env = ConfigureEnvironment(self)
        self.run("cd coin-clp && {} ./configure".format(env.command_line_env))
        self.run("cd coin-clp && {} make".format(env.command_line_env))

    def package(self):
        self.copy("*.hpp", dst="include", src="coin-clp/Osi/src")
        self.copy("*.hpp", dst="include", src="coin-clp/Clp/src")
        self.copy("*.hpp", dst="include", src="coin-clp/CoinUtils/src")
        self.copy("libOsi.so*", dst="lib", src="coin-clp/Osi/src/Osi/.libs")
        self.copy("libClp.so*", dst="lib", src="coin-clp/Clp/src/.libs")
        self.copy("libClpSolver.so*", dst="lib", src="coin-clp/Clp/src/.libs")
        self.copy("libCoinUtils.so*", dst="lib", src="coin-clp/CoinUtils/src/.libs")

    def package_info(self):
        self.cpp_info.libs = ["Osi", "Clp", "ClpSolver", "CoinUtils"]
