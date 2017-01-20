class foo {
    private:
        String myPrivateString;
    protected:
        String myProtectedString;
    public:
        String myPublicString;
        void foo_method() {
            std::cout << "foo" << std::endl;
        }
}

int main()
{
  int wrongName = 1;
  return wrongName;
}

void foo_function() {
}