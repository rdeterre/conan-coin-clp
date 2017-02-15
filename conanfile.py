from conans import ConanFile, ConfigureEnvironment

class ConanCointClp(ConanFile):
    name = "coin-clp"
    version = "0.1"
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
        self.copy("*.hpp", dst="include", src="Osi/src")
        self.copy("*.hpp", dst="include", src="Clp/src")
        self.copy("*.hpp", dst="include", src="CoinUtils/src")
        self.copy("libOsi.so*", dst="lib", src="Osi/src/Osi/.libs")
        self.copy("libClp.so*", dst="lib", src="Clp/src/.libs")
        self.copy("libClpSolver.so*", dst="lib", src="Clp/src/.libs")
        self.copy("libCoinUtils.so*", dst="lib", src="CoinUtils/src/.libs")

    def package_info(self):
        self.cpp_info.libs = ["Osi", "Clp", "ClpSolver", "CoinUtils"]