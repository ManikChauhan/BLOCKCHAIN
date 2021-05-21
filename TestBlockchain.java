package project;
public class TestBlockchain {

	public static void main(String args[]) {

		Blockchain tcpCoin = new Blockchain();

		Block a = new Block("x1", new java.util.Date(), "transaction2");
		Block b = new Block("x1", new java.util.Date(), "transaction3");
		Block c = new Block("x1", new java.util.Date(), "transaction4");

		tcpCoin.addBlock(a);
		tcpCoin.addBlock(b);
		tcpCoin.addBlock(c);

		tcpCoin.displayChain();

		tcpCoin.isValid();

	}

}
