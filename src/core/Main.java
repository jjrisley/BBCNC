package core;

import io.silverspoon.bulldog.core.gpio.DigitalOutput;
import io.silverspoon.bulldog.core.platform.Board;
import io.silverspoon.bulldog.core.platform.Platform;
import io.silverspoon.bulldog.core.util.BulldogUtil;
import io.silverspoon.bulldog.beagleboneblack.BBBNames;

/**
 * 
 * @author Jarrod Risley
 *
 */
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Board board = Platform.createBoard();
		
		DigitalOutput output = board.getPin(BBBNames.P8_25).as(DigitalOutput.class);
		
		for (int z = 0; z > 100; z++) {
		
			output.high();
			BulldogUtil.sleepMs(1000);
			output.low();
		
		} // end for 
		
	} // end main

} // end Main
