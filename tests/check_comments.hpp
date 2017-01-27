/**
 * @brief This is a brief description of Foo.
 *
 * It has no more use than to be an example for
 * commented code.
 *
 * It has a very huge comment.
 */
class Foo {
public:
    /**
     * @brief members should have brief description.
     */
    int public_member;
    /**
     * @brief methods should have a brief
     * description.
     * @param parameter should be described.
     * @return a value
     */
    int public_method(int parameter);
protected:
    /**
     * @brief members should have brief description.
     */
    int protected_member;
    /**
     * @brief methods should have a brief description.
     * @param parameter should be described.
     * @return a value
     */
    int protected_method(int parameter);
private:
    /**
     * @brief members should have brief description.
     */
    int private_member;
    /**
     * @brief methods should have a brief description.
     * @param parameter should be described.
     * @return a value
     */
    int private_method(int parameter);
}

class Bar {
public:
    int public_member;
    int public_method(int parameter);
protected:
    int protected_member;
    int protected_method(int parameter);
private:
    int protected_member;
    int protected_method(int parameter);
}

/**
 * @brief Brief description.
 *
 * Extended description
 */
struct FooStruct {
    /**
    * @brief description.
    */
    int foo;
}

struct BarStruct {
    int foo;
}
